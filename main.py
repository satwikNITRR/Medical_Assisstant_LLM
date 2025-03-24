import streamlit as st
import google.genai as genai
import PIL.Image


prompt="""As per your knowledge i want the response. As a highly skilled medical practitioner specializing in image analysis, you are tasked with examining medical images for a renowned hospital. Your expertise is crucial in identifying any anomalies, diseases, or health issues that may be present in the images.

Your Responsibilities include:
1.Detailed Analysis: Thoroughly analyze each image, focusing on identifying any abnormal findings.
2.Findings Report: Document all observed anomalies or signs of disease. Clearly articulate these findings in a structured format.
3.Recommendations and Next Steps: Based on your analysis, suggest potential next steps, including further tests or treatments as applicable.
4.Treatment Suggestions: If appropriate, recommend possible treatment options or interventions.

Important Notes:
1.Scope of Response: Only respond if the image pertains to human health issues.
2.Clarity of Image: In cases where the image quality impedes clear analysis, note that certain aspects are "Unable to be determined based on the provided image."

Disclaimer: Accompany your analysis with the disclaimer: "Consult with a Doctor before making any decisions."
Your insights are invaluable in guiding clinical decisions. Please proceed with the analysis, adhering to the structured approach outlined above.

Please provude me an output response with these 4 headings Detailed Analysis,Findings Report,Recommendations and Next Steps and Treatment Suggestions"""

def generate():
    client = genai.Client(api_key="AIzaSyACO6CDnGd20ZufK4gdR1e43zTUr9MbbZY")
    model="gemini-2.0-flash"
    contents = [
            genai.types.Content(
                role="user",
                parts=[
                    genai.types.Part.from_bytes(
                        mime_type="""image/jpeg""",
                        data=image_data
                    ),
                    #prompt
                    genai.types.Part.from_text(text=prompt),
                ],
            )
    ]
    generate_content_config = genai.types.GenerateContentConfig(
            temperature=1,
            top_p=0.95,
            top_k=40,
            max_output_tokens=8192,
            response_mime_type="text/plain",
        )

    response = ""
    for chunk in client.models.generate_content_stream(
            model=model,
            contents=contents,
            config=generate_content_config,
        ):
        response += chunk.text
    
    return response

st.title("DiagnoSense")
st.header("Your Own AI Diagnistic Budy ")
file=st.file_uploader("choose a file" ,type=["png","jpg","jpeg"])
if file:
    st.image(file.getvalue(),caption="uploaded image")

press_button=st.button("Press to know more")
if press_button:
    image_data=file.getvalue()
    a=generate()
    st.title("Here is the analaysis based on your image : ")
    st.write(a)

# if __name__=="__main__":
#     generate()

