from flask import Flask, render_template, redirect, url_for
from roster import ROSTER

app = Flask(__name__)
#app.config['SECRET_KEY'] = '14uff!eumps&w00ze!s'
application = app
#get all of the IDs and names and append them to the list names
def get_names(source):
    names = []
    for row in source:
        id = row["id"]
        name = row["name"]
        photo = row["photo"]
        names.append([id, name])
    return names, photo

# get the information for each ID
def get_inmatedata(source, id):
    for row in source:
        if id == str( row["id"] ):
            # decode handles accented characters
            name = row["name"] 
            race = row["race"]
            photo = row["photo"] 
            sex = row["sex"]
            dob = row["dob"]
            entry = row["entry"]
            facility = row["facility"]
            custody = row["custody"]
    return id, name, race, photo, sex, dob, entry, facility, custody

#set the homepage and the /restaurants.html to run the function to get information using the python dictionary INSPECTIONS
@app.route('/')
@app.route('/inmates.html')
def inmates():
    names, photo = get_names(ROSTER)
    return render_template('inmates.html', pairs=names, photo=photo)



#make a path for the /restaurant with each restaurant id and show the information for each restaurant with each ID
@app.route('/inmate/<id>.html')
def inmate(id):
    id, name, race, photo, sex, dob, entry, facility, custody = get_inmatedata(ROSTER, id)
    return render_template('inmate.html', pairs=name, name=name, race=race, photo=photo, sex=sex, dob=dob, entry=entry, facility=facility, custody=custody)

if __name__ == '__main__':
    app.run(debug=True)
