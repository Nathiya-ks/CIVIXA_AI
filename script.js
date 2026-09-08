// ================= SET EXAMPLE QUERY =================

function setQuery(text) {

    document.getElementById("query").value = text;

}



// ================= SEARCH SERVICE =================

async function searchService() {


    const query = document
        .getElementById("query")
        .value
        .trim();


    if (query === "") {

        alert("Please enter your requirement.");

        return;

    }


    // Show loading message

    document.getElementById("result").innerHTML = `

        <div class="card">

            <h2>🤖 CIVIXA AI is thinking...</h2>

            <p>

                Understanding your requirement

                and finding a suitable service.

            </p>

        </div>

    `;


    try {


        const response = await fetch(

            "/api/search",

            {

                method: "POST",

                headers: {

                    "Content-Type":
                    "application/json"

                },

                body: JSON.stringify({

                    query: query

                })

            }

        );


        const data = await response.json();


        // Create application steps

        let stepsHTML = "";


        data.steps.forEach(

            function(step) {

                stepsHTML +=

                    `<li>${step}</li>`;

            }

        );


        // Display result

        document.getElementById("result").innerHTML = `

            <div class="card">


                <h2>

                    🎯 ${data.name}

                </h2>


                <p>

                    ${data.description}

                </p>


                <h3>

                    ✅ Eligibility

                </h3>


                <p>

                    ${data.eligibility}

                </p>


                <h3>

                    📄 Documents Required

                </h3>


                <p>

                    ${data.documents}

                </p>


                <h3>

                    📋 Application Steps

                </h3>


                <ol>

                    ${stepsHTML}

                </ol>


                <a

                    href="${data.link}"

                    target="_blank"

                    class="official-link">

                    🔗 Visit Official Website

                </a>


            </div>

        `;


        // Scroll to result

        document.getElementById(

            "result-section"

        ).scrollIntoView({

            behavior: "smooth"

        });


    }

    catch (error) {


        document.getElementById("result").innerHTML = `

            <div class="card">

                <h2>⚠️ Something went wrong</h2>

                <p>

                    Please make sure the Flask server

                    is running.

                </p>

            </div>

        `;


        console.error(error);

    }

}



// ================= VOICE INPUT =================

function startVoice() {


    const SpeechRecognition =

        window.SpeechRecognition ||

        window.webkitSpeechRecognition;


    if (!SpeechRecognition) {

        alert(

            "Voice recognition is not supported in this browser."

        );

        return;

    }


    const recognition =

        new SpeechRecognition();


    recognition.lang = "en-IN";


    recognition.start();


    recognition.onstart = function() {

        console.log(

            "Voice recognition started"

        );

    };


    recognition.onresult = function(event) {


        const text =

            event.results[0][0].transcript;


        document.getElementById(

            "query"

        ).value = text;


    };


    recognition.onerror = function(event) {

        console.log(

            "Voice error:",

            event.error

        );

    };

}