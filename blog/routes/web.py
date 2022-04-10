from webbrowser import get
from flask import render_template, redirect, flash, url_for, session, request, abort
from flask_login import current_user, login_user, logout_user, login_required
from blog import app, db
from blog.forms import LoginForm, PostForm, UserForm, CommentForm, SettingsForm
from blog.models import User, Post, Comment, Role, Setting
from blog.utils import title_slugifier, img_upload
import datetime


@app.route("/")
def homepage():
    settings = Setting.query.all()
    posts = Post.query.order_by(Post.id.desc()).paginate(1, 7, True)
    return render_template("index.html", posts=posts, current_user=current_user, settings=settings)

@app.route("/blog")
def blog():
    settings = Setting.query.all()
    page_number = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.id.desc()).paginate(page_number, 10, True)

    if posts.has_next:
        next_page = url_for('blog', page=posts.next_num)
    else:
        next_page = None

    if posts.has_prev:
        prev_page = url_for('blog', page=posts.prev_num)
    else:
        prev_page = None

    return render_template("blog.html", posts=posts, current_user=current_user, prev_page=prev_page, next_page=next_page, settings=settings)

@app.route("/post/<string:slug>", methods=["POST", "GET"])
def post_detail(slug):
    settings = Setting.query.all()
    form = CommentForm()
    post = Post.query.filter_by(slug=slug).first_or_404()
    if form.validate_on_submit():
        if current_user.is_authenticated:
            if Comment.query.filter_by(post_id=post.id, author_id=current_user.id):
                return redirect(url_for('post_detail', slug=slug))
            new_comment = Comment(author_id=current_user.id, post_id=post.id, content=form.content.data)
            db.session.add(new_comment)
            db.session.commit()

    comments = Comment.query.filter_by(post_id=post.id).all()

    showTextarea = True
    i = 0
    while i<len(comments):
        user = User.query.get(comments[i].author_id)
        if user.id == current_user.id:
            showTextarea = False
        comments[i].user = user
        i += 1

    return render_template('post.html', post=post, form=form, comments=comments, showTextarea=showTextarea, settings=settings)

@app.route("/login", methods=["POST", "GET"])
def login():
    settings = Setting.query.all()
    if current_user.is_authenticated:
        return redirect(url_for('homepage'))
    else:
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user is None or not user.check_password(form.password.data):
                flash('email e password non combaciano!')
                return redirect(url_for('login'))
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('homepage'))
    return render_template("login.html", form=form, current_user=current_user, settings=settings)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('homepage'))

@app.route("/register", methods=["POST", "GET"])
def register():
    settings = Setting.query.all()
    if current_user.is_authenticated:
        return redirect(url_for('homepage'))
    form = UserForm()
    if form.validate_on_submit():
        password = User.password_hash(form.password.data)
        new_user = User(username=form.username.data, email=form.email.data, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('homepage'))
    return render_template("register.html", current_user=current_user, form=form, settings=settings)

@app.route("/profile")
def profile():
    settings = Setting.query.all()
    role = Role.query.get(current_user.role_id)
    return render_template("profile.html", current_user=current_user, role=role, settings=settings)

@app.route("/profile/edit", methods=["POST", "GET"])
def profile_edit():
    settings = Setting.query.all()
    if current_user.is_authenticated:
        form = UserForm()
        if form.validate_on_submit():
            if current_user.check_password(form.password.data):
                user = User.query.get(current_user.id)
                user.username = form.username.data
                user.email = form.email.data
                if form.new_password.data:
                    user.set_password_hash(form.new_password.data)
                
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('profile'))
            else:
                flash('Password errata')
                return redirect(url_for('profile_edit'))
        form.username.data = current_user.username
        form.email.data = current_user.email
        return render_template("profileedit.html", current_user=current_user, form=form, settings=settings)

@app.route("/admin")
def admin():
    settings = Setting.query.all()
    if current_user.is_authenticated:
        if current_user.role_id == 2:
            return render_template("/admin/dashboard.html", current_user=current_user, now=datetime.datetime.now(), settings=settings)
        elif current_user.role_id == 3:
            return redirect(url_for('posts'))

    return redirect(url_for('homepage'))


@app.route("/admin/posts")
def posts():
    settings = Setting.query.all()
    if current_user.is_authenticated:
        if current_user.role_id == 2 or current_user.role_id == 3:
            if current_user.role_id == 2:
                posts = Post.query.all()
            else:
                posts = Post.query.filter(Post.author_id == current_user.id).all()

            return render_template("/admin/posts.html", current_user=current_user, posts=posts, settings=settings)

    return redirect(url_for('homepage'))

@app.route("/admin/post/create", methods=["POST", "GET"])
def post_create():
    settings = Setting.query.all()
    if current_user.is_authenticated:
        if current_user.role_id == 2 or current_user.role_id == 3:
            form = PostForm()
            if form.validate_on_submit():
                new_post = Post(title=form.title.data, subtitle=form.subtitle.data, content=form.content.data, author_id=current_user.id, slug=title_slugifier(form.title.data))
                if form.image.data:
                    try:
                        image = img_upload(form.image.data)
                        new_post.image = image
                    except Exception:
                        flash("C'è stato un problema nell'upload del background")
                if form.card_cover.data:
                    try:
                        card_cover = img_upload(form.card_cover.data)
                        new_post.card_cover = card_cover
                    except Exception:
                        flash("C'è stato un problema nell'upload della cover")

                db.session.add(new_post)
                db.session.commit()
                return redirect(url_for('posts'))

            return render_template("/admin/post.html", current_user=current_user, form=form, settings=settings)

        return redirect(url_for('homepage'))

@app.route('/admin/post/<int:post_id>/edit', methods=["POST", "GET"])
def post_edit(post_id):
    settings = Setting.query.all()
    if current_user.is_authenticated:
        if current_user.role_id == 2 or current_user.role_id == 3:
            post = Post.query.get_or_404(post_id)
            if post.author_id == current_user.id or current_user.role_id == 2:
                form = PostForm()
                if form.validate_on_submit():
                    post.title = form.title.data
                    post.subtitle = form.subtitle.data
                    post.content = form.content.data

                    if form.image.data:
                        try:
                            image = img_upload(form.image.data)
                            post.image = image
                        except Exception:
                            flash("C'è stato un problema nell'upload del background")
                    if form.card_cover.data:
                        try:
                            card_cover = img_upload(form.card_cover.data)
                            post.card_cover = card_cover
                        except Exception:
                            flash("C'è stato un problema nell'upload della cover")
                    
                    db.session.commit()
                    return redirect(url_for('posts'))

                form.title.data = post.title
                form.subtitle.data = post.subtitle
                form.content.data = post.content
                return render_template("/admin/post.html", current_user=current_user, form=form, settings=settings)
            else: 
                abort(403)

    return redirect(url_for('homepage'))

@app.route('/admin/post/<int:post_id>/delete', methods=["POST", "GET"])
@login_required
def delete(post_id):
    if current_user.role_id == 2 or current_user.role_id == 3:
        post = Post.query.get_or_404(post_id)
        if post.author_id == current_user.id or current_user.role_id == 2:
            db.session.delete(post)
            db.session.commit()
            return redirect(url_for('posts'))
        else: 
            abort(403)

    return redirect(url_for('homepage'))
    
                

@app.route("/admin/users")
def users():
    settings = Setting.query.all()
    if current_user.is_authenticated:
        if current_user.role_id == 2:
            users = User.query.all()
            return render_template("/admin/users.html", current_user=current_user, users=users, settings=settings)

    return redirect(url_for('homepage'))

@app.route("/admin/user/<int:user_id>/edit", methods=["POST", "GET"])
def admin_user_edit(user_id):
    settings = Setting.query.all()
    if current_user.is_authenticated:
        if current_user.role_id == 2:
            user = User.query.get_or_404(user_id)
            form = UserForm()
            form.password.data = user.password
            if form.validate_on_submit():
                user.username = form.username.data
                user.email = form.email.data
                user.role_id = form.role_id.data
                db.session.commit()
                return redirect(url_for('users'))
     
            form.role_id.choices = [(role.id, role.role_name) for role in Role.query.all()]
            form.role_id.default = user.role_id
            form.process()
            form.username.data = user.username
            form.email.data = user.email
            return render_template("/admin/useredit.html", current_user=current_user, form=form, settings=settings)
    
    return redirect(url_for('homepage'))


@app.route('/admin/user/<int:user_id>/delete')
def user_delete(user_id):
    if current_user.is_authenticated:
        if current_user.role_id == 2:
            user = User.query.get_or_404(user_id)
            db.session.delete(user)
            db.session.commit()
            return redirect(url_for('users'))

    return redirect(url_for('homepage'))

@app.route('/admin/settings', methods=["POST", "GET"])
def settings():
    settings = Setting.query.all()
    if current_user.is_authenticated:
        if current_user.role_id == 2:
            form = SettingsForm()
            if form.validate_on_submit():
                data = [form.blog_name.data, form.blog_motto.data, form.blog_title_homepage.data, form.blog_subtitle_homepage.data]
                i = 0
                for setting in settings:
                    setting.value_setting = data[i]
                    db.session.add(setting)
                    db.session.commit()
                    i += 1
                    
                return redirect(url_for('settings'))
            else:
                form.blog_name.data = settings[0].value_setting
                form.blog_motto.data = settings[1].value_setting
                form.blog_title_homepage.data = settings[2].value_setting
                form.blog_subtitle_homepage.data = settings[3].value_setting
                return render_template("/admin/settings.html", current_user=current_user, form=form, settings=settings)

    return redirect(url_for('homepage'))