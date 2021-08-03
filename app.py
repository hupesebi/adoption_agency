from flask import Flask, request, redirect, render_template
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "SECRET!"

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()


debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

@app.route('/', methods=['GET', 'POST'])
def show_pets():
    """Shows all pets"""

    pets = Pet.query.all()
    return render_template('/pets.html', pets = pets)


@app.route('/add', methods=['GET', 'POST'])
def add_pets():
    """Page with a form to add a pet"""

    form = AddPetForm()

    if form.validate_on_submit():
        data = {k:v for k,v in form.data.items() if k != 'csrf_token'}
        newPet = Pet(**data)
        db.session.add(newPet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template("add_pet.html", form=form)

@app.route('/<int:id>', methods = ['GET', 'POST'])
def show_pet_details(id):
    """Page that shows the details for each pet and allows to update certain fields"""
    
    pet = Pet.query.get_or_404(id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        return redirect('/')

    else:
        return render_template('/pet_edit.html', form = form, pet = pet)


    


