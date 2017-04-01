from flask import Flask, render_template, redirect, url_for
from inspections import INSPECTIONS


app = Flask(__name__)

#get all of the IDs and names and append them to the list names
def get_names(source):
    names = []
    for row in source:
        id = row["ID"]
        name = row["Name"]
        names.append([id, name])
    return names

# get the information for each ID
def get_restaurantdata(source, id):
    for row in source:
        if id == str( row["ID"] ):
            # decode handles accented characters
            name = row["Name"] 
            address = str (row["Address"] )
            zip = row["Zip"]
            date = row["Date"]
            result = row["Result"]
            return id, name, address, zip, date, result

#set the homepage and the /restaurants.html to run the function to get information using the python dictionary INSPECTIONS
@app.route('/')
@app.route('/restaurants.html')
def restaurants():
    names = get_names(INSPECTIONS)
    return render_template('restaurants.html', pairs=names)



#make a path for the /restaurant with each restaurant id and show the information for each restaurant with each ID
@app.route('/restaurant/<id>')
def restaurant(id):
    id, name, address, zip, date, result = get_restaurantdata(INSPECTIONS, id)
   
    return render_template('inspection.html', name=name, address=address, zip=zip, date=date, result=result)

if __name__ == '__main__':
    app.run(debug=True)
