from flask import Flask, render_template, redirect, url_for
from inspections import INSPECTIONS


app = Flask(__name__)
app.config['SECRET_KEY'] = '14uff!eumps&w00ze!s'
#Bootstrap(app)
# this turns file-serving to static, using Bootstrap files installed in env
# instead of using a CDN
#app.config['BOOTSTRAP_SERVE_LOCAL'] = True
# for WSGI
# application = app


# define two functions to be used by the routes

# retrieve all the titles from the dataset and put them into a list
def get_names(source):
    names = []
    for row in source:
        id = row["ID"]
        name = row["Name"]
        names.append([id, name])
    return names

# find the row that matches the title in the URL, retrieve author and year
def get_restaurantdata(source, id):
    for row in source:
        if id == str( row["ID"] ):
            # decode handles accented characters
            name = row["Name"]
            address = row["Address"]
            zip = row["Zip"]
            date = row["Date"]
            result = row["Result"]
            return id, name, address, zip, date, result


@app.route('/')
@app.route('/restaurants.html')
def restaurants():
    names = get_names(INSPECTIONS)
    # pass the sorted list of titles to the template
    return render_template('restaurants.html', pairs=names)




@app.route('/restaurant/<id>')
def restaurant(id):
    id, name, address, zip, date, result = get_restaurantdata(INSPECTIONS, id)
    # pass the data for the selected book to the template
    return render_template('inspection.html', name=name, adddress=address, zip=zip, date=date, result=result)

if __name__ == '__main__':
    app.run(debug=True)
