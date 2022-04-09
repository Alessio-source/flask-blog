from webbrowser import get
from flask import render_template, redirect, flash, url_for, session, request, abort
from flask_login import current_user, login_user, logout_user, login_required
from blog import app, db
from blog.forms import LoginForm, PostForm, RegisterForm
from blog.models import User, Post
from blog.utils import title_slugifier, img_upload
import datetime

@app.route("/")
def homepage():
    posts = Post.query.all()
    return render_template("index.html", posts=posts, current_user=current_user)

@app.route("/post/<string:slug>")
def post_detail(slug):
    post = Post.query.filter_by(slug=slug).first_or_404()
    return render_template('post.html', post=post)

@app.route("/login", methods=["POST", "GET"])
def login():
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
    return render_template("login.html", form=form, current_user=current_user)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('homepage'))

@app.route("/register", methods=["POST", "GET"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('homepage'))
    form = RegisterForm()
    if form.validate_on_submit():
        password = User.password_hash(form.password.data)
        new_user = User(username=form.username.data, email=form.email.data, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('homepage'))
    return render_template("register.html", current_user=current_user, form=form)

@app.route("/profile")
def profile():
    return render_template("profile.html", current_user=current_user)

@app.route("/admin")
def admin():
    if current_user.is_authenticated:
        if current_user.role_id == 2:
            return render_template("/admin/dashboard.html", current_user=current_user, now=datetime.datetime.now())
        elif current_user.role_id == 3:
            return redirect(url_for('posts'))

    return redirect(url_for('homepage'))


@app.route("/admin/posts")
def posts():
    if current_user.is_authenticated:
        if current_user.role_id == 2 or current_user.role_id == 3:
            if current_user.role_id == 2:
                posts = Post.query.all()
            else:
                posts = Post.query.filter(Post.author_id == current_user.id).all()

            return render_template("/admin/posts.html", current_user=current_user, posts=posts)

    return redirect(url_for('homepage'))

@app.route("/admin/post/create", methods=["POST", "GET"])
def post_create():
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

            return render_template("/admin/post.html", current_user=current_user, form=form)

        return redirect(url_for('homepage'))

@app.route('/admin/post/<int:post_id>/edit', methods=["POST", "GET"])
def post_edit(post_id):
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
                return render_template("/admin/post.html", current_user=current_user, form=form)
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
    if current_user.is_authenticated:
        if current_user.role_id == 2:
            users = User.query.all()
            return render_template("/admin/users.html", current_user=current_user, users=users)

    return redirect(url_for('homepage'))