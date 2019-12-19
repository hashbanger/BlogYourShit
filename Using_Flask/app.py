from flask import Flask, render_template, flash, redirect, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'b033b0296b67a3fd1cf2e19b329e8bcf'
posts = [
    {
        'author':'Prashant Brahmbhatt',
        'title': 'The Seven Sins',
        'content': 'lorem ipsum lorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsum',
        'date_posted':'April 20,2019'
    },
    {
        'author':'Jon Doe',
        'title': 'The life of a writer',
        'content': 'lorem ipsum lorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsum',
        'date_posted':'September 22,2020'
    }
]

@app.route('/')
def home():
    return render_template('home.html', posts = posts)

@app.route('/about')
def about():
    return render_template('about.html', title = 'About')

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Account created for {}'.format(form.username.data), category = 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form= form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'prashant.brahmbhatt32@outlook.com' and form.password.data == 'password':
            flash('You have successfully logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username/password', 'danger')
    return render_template('login.html', title = 'Login', form = form)

if __name__ == "__main__":
    app.run(debug = True)