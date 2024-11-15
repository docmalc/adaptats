from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/get-user/<user_id>")
#@app.route("/parseResume/<companyId>/<resumeUrl>")
@app.route("/parseResume/<resume_url>")
def get_user(resume_url):
    
    # Get resume from resumeUrl

    # Parse resume for name, phone number, email

    # Return parsedCandidateData
    
    
    user_data = {
        "user_id": resume_url,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra
    
    return jsonify(user_data), 200


# /get-user/123?extra="hello"


if __name__=="__main__":
    app.run(debug=True)