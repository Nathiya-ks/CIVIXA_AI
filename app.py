from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_folder="templates/static")


# ---------------- HOME PAGE ----------------

@app.route("/")
def home():
    return render_template("index.html")


# ---------------- AI SERVICE SEARCH ----------------

@app.route("/api/search", methods=["POST"])
def search_service():

    data = request.get_json()

    query = data.get("query", "").lower().strip()


    # -------- FARMER --------

    if (
        "farmer" in query
        or "agriculture" in query
        or "farming" in query
        or "crop" in query
        or "விவசாய" in query
    ):

        result = {

            "name": "PM-KISAN",

            "description":
            "Financial assistance scheme for eligible farmers.",

            "eligibility":
            "Eligible farmer families subject to applicable scheme rules.",

            "documents":
            "Aadhaar, bank account details and land records.",

            "steps": [

                "Visit the official PM-KISAN portal",

                "Register your details",

                "Enter the required information",

                "Submit the application",

                "Track your application status"

            ],

            "link":
            "https://pmkisan.gov.in/"

        }


    # -------- STUDENT --------

    elif (
        "student" in query
        or "scholarship" in query
        or "education" in query
        or "college" in query
        or "school" in query
        or "மாணவர்" in query
        or "கல்வி" in query
    ):

        result = {

            "name": "Scholarship Assistance",

            "description":
            "Financial assistance opportunities for eligible students.",

            "eligibility":
            "Eligibility depends on the applicable scholarship category and rules.",

            "documents":
            "Aadhaar, income certificate, educational certificates and bank details.",

            "steps": [

                "Select the appropriate scholarship",

                "Register on the portal",

                "Enter student details",

                "Upload required documents",

                "Submit the application"

            ],

            "link":
            "https://scholarships.gov.in/"

        }


    # -------- HEALTH --------

    elif (
        "health" in query
        or "hospital" in query
        or "medical" in query
        or "medicine" in query
        or "doctor" in query
        or "மருத்துவம்" in query
    ):

        result = {

            "name": "Ayushman Bharat",

            "description":
            "Health coverage assistance for eligible beneficiaries.",

            "eligibility":
            "Eligibility depends on the applicable beneficiary criteria.",

            "documents":
            "Aadhaar or other accepted identity documents.",

            "steps": [

                "Check eligibility",

                "Verify beneficiary details",

                "Find the appropriate service",

                "Access eligible healthcare benefits"

            ],

            "link":
            "https://pmjay.gov.in/"

        }


    # -------- AADHAAR --------

    elif (
        "aadhaar" in query
        or "aadhar" in query
        or "identity" in query
        or "address update" in query
        or "ஆதார்" in query
    ):

        result = {

            "name": "Aadhaar Services",

            "description":
            "Services related to Aadhaar enrolment and updates.",

            "eligibility":
            "Available services depend on the Aadhaar service requested.",

            "documents":
            "Aadhaar details and supporting documents where required.",

            "steps": [

                "Identify the required Aadhaar service",

                "Check the applicable requirements",

                "Complete the request",

                "Track the service status"

            ],

            "link":
            "https://uidai.gov.in/"

        }


    # -------- NO MATCH --------

    else:

        result = {

            "name": "No Matching Service Found",

            "description":
            "CIVIXA AI could not find a matching service. Please describe your requirement using simple words.",

            "eligibility":
            "Not available.",

            "documents":
            "Not available.",

            "steps": [

                "Try describing your need again",

                "Example: I am a farmer and need financial assistance",

                "Example: I am a student looking for scholarship",

                "Example: I need health assistance"

            ],

            "link":
            "#"

        }


    return jsonify(result)


# ---------------- RUN APPLICATION ----------------

if __name__ == "__main__":

    app.run(debug=True)