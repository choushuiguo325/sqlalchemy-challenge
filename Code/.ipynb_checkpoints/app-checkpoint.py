step 2 - climate analysis

from flask import Flask,jsonify

app = Flask("__name__")

@app.route("/")
def home():
    return "Hi"


# @app.route("/")
# def home_page():
#         print('''
#         1. Query Precipitation Data: /api/v1.0/precipitation
#         2. Query Station Data: /api/v1.0/stations
#         3. Query Temperature Data: /api/v1.0/tobs
#         4. Query Temperature Description for A Given Start: /api/v1.0/<start>
#         5. Query Temperature Description for A Given Start-end Range: /api/v1.0/<start>/<end>
        
#         ''')
#         return "Welcome to our query 'home' page!"
        
        
# @app.route("/api/v1.0/precipitation")
# def precipitation():
        
#     return jsonify(precipitation_df)
    
        
# @app.route("/api/v1.0/stations")
# def stations():
                
#     return
    
    
# @app.route("/api/v1.0/tobs")
# def tobs():
                
#     return

# @app.route("/api/v1.0/<start>")
# def temp_start():
                
#     return
    
    
# @app.route("/api/v1.0/<start>/<end>")
# def temp_range():
                
#     return
    
if __name__ == "__main__":
    app.run(debug=True)