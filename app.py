import pandas as pd
from flask import Flask,request,jsonify, render_template,url_for

app=Flask(__name__)
df = pd.read_csv('Medicine_Details.csv')

def get_composition(medicineName):
    # Filter the DataFrame based on the 
    filtered_df = df[df['MedicineName'] == medicineName]
    if not filtered_df.empty:
        composition = filtered_df['Composition'].iloc[0]  # Assuming 'Composition' is the column containing composition information
        return composition
    else:
        return None

@app.route('/', methods=['GET'])
def index():
  return render_template('index.html')


def searchMedicine():
   medicineName = request.args.get('medicineName')
   composition = get_composition(medicineName)  # Implement this function
   return {'medicineName': medicineName, 'composition': composition}



#@app.route('/search', methods=['GET'])
#def index():
#    return render_template('index.html')
#def search_medicine():
#
#    print("Request URL:", request.url)
#    print("Query Parameters:", request.args)
#
#    # Get the medicine name from the request query parameters
#    medicine_name = request.args.get('medicine_name')
#    
#    # Lookup the composition for the provided medicine name
#    composition = medicine_data.get(medicine_name.lower())
#    
#    # Return the composition as JSON response
#    if composition:
#        return jsonify({'composition': composition})
#    else:
#        return jsonify({'composition': 'Composition not found'})
#

if __name__=="__main__":
    app.run(debug=True)