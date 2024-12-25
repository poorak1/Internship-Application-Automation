import google.generativeai as genai


resume='''
YOUR BASE RESUME in HTML/CSS FORMAT
'''
NAMEE = "Your Name"

def modify_resume(intern_desc, skills=" ", current_resume=resume):

    api_keyy="YOUR GEMINI API KEY"
    genai.configure(api_key=api_keyy)

    model = genai.GenerativeModel("gemini-1.5-flash")
    PROMPT = f'''Consider yourself an an expert resume builder, you are given a resume in html format and the internship 
    description which has the desired keywords.You need to modify the html resume content with respect to the internship description and
    skills required without changing the styling of the resume and just output a modified html resume. internship description is {intern_desc} 
    , skills required is {skills} and resume is {current_resume}. Just output the modified html resume based upon the information given
    without including any self fillable information or any information that has to be filled up by me later. Do not change anything in the projects section.
    Nothing except the modified hmtl resume should be outputted.''' 
    response = model.generate_content(PROMPT)
    #print(response.text)
    #return response.text


    test_response = response.text.split("\n")
    if test_response[0] == "```html":
        if(test_response[-2] == "```"):
            test_response = "\n".join(test_response[1:-2])
        else:
            test_response = "\n".join(test_response[1:-1])
        return test_response
    else:
        return response.text


def cover_letter(job_description, current_resume=resume):
    api_keyy="YOUR GEMINI API KEY"
    genai.configure(api_key=api_keyy)

    model = genai.GenerativeModel("gemini-1.0-pro")
    PROMPT = f'''Consider yourself an an expert cover letter writer, you need to write a cover letter for {NAMEE}'s internship in 
    first person point of view. All the basic detail's of {NAMEE} can be taken from his resume. {NAMEE}'s resume is {current_resume} 
    and the internship description is {job_description}. Just output a cover letter incorporating the resume and job description 
    in 200-250 words in text format. Start by greeting "Hello Sir". Do not include any information that has to be filled by me. ''' 
    
    
    response = model.generate_content(PROMPT)
    #print(response.text)
    return response.text

