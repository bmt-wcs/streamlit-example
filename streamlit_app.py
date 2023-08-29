import extra_streamlit_components as stx
import streamlit as st
import openai
import re

quests_data = [
    {
        "id": 2090,
        "title": "Express 04 - 🛸 PUT method and data modification",
        "subTitle": "PUT method and data modification",
        "completionTime": 4,
        "questLink": "assets/quests/express-quest.txt"
    },
    {
        "id": 2095,
        "title": "AWS Glue ETL Part 2",
        "subTitle": "AWS Glue ETL Part 2",
        "completionTime": 3,
        "questLink": "https://questlink2.com"
    },
    {
        "id": 2214,
        "title": "AWS Lambda Overview",
        "subTitle": "Introduction to Lambda functions in AWS",
        "completionTime": 2,
        "questLink": "https://questlink3.com"
    }
]

openai.api_key = "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"

# Sidebar layout
st.sidebar.title("Future Group LMS")

st.sidebar.markdown(
    '<a href="/" class="menu-item" target="_self">Students</a>', unsafe_allow_html=True)
st.sidebar.markdown(
    '<a href="/?nav=/teachers" class="menu-item" target="_self">Teachers</a>', unsafe_allow_html=True)


def init_router():
    return stx.Router({"/": quests, "/teachers": queststeachers, "/createquest": createquest})


def quests():

    st.title("Students Dashboard")

    # Load the custom CSS from the file
    with open("assets/styles/quest-styles.css", "r") as f:
        custom_css = f.read()

    # Set the custom CSS for the entire app
    st.markdown(f"<style>{custom_css}</style>", unsafe_allow_html=True)

    # Horizontal card layout
    col1, col2 = st.columns(2)

    for index, item in enumerate(quests_data):
        if index % 2 == 0:
            col = col1
        else:
            col = col2

        with col:
            st.markdown(f"""<div class="card">
                   <div class="empty-star">&#9734;</div> <!-- Empty star icon -->
                    <div class="card-header">
                    {item['title']}
                    </div>
                    <div class="card-body">
                    {item['subTitle']}
                    </div>
                    <div class="card-footer">
                     <div >
                        <svg class="bottom-left-icons" xmlns="http://www.w3.org/2000/svg" width="20" height="20">
                                    <path fill="#FFFFFF" d="m5.2494 8.0688 2.83-2.8269 14.1343 14.15-2.83 2.8269zm4.2363-4.2415 2.828-2.8289 5.6577 5.656-2.828 2.8289zM.9989 12.3147l2.8284-2.8285 5.6569 5.6569-2.8285 2.8284zM1 21h12v2H1z"></path>
                                </svg> 
                                 <svg class="bottom-left-icons" xmlns="http://www.w3.org/2000/svg" width="20" height="20">
                                    <path fill="#FFFFFF" d="M15 1H9v2h6V1zm-4 13h2V8h-2v6zm8.03-6.61 1.42-1.42c-.43-.51-.9-.99-1.41-1.41l-1.42 1.42C16.07 4.74 14.12 4 12 4c-4.97 0-9 4.03-9 9s4.02 9 9 9 9-4.03 9-9c0-2.12-.74-4.07-1.97-5.61zM12 20c-3.87 0-7-3.13-7-7s3.13-7 7-7 7 3.13 7 7-3.13 7-7 7z"></path>
                                </svg> 
                               <span class="bottom-left-text">{item['completionTime']}h</span>
                            </div> 
                     <a class="btn-right" href='/?nav=/questdetail/{item['id']}' target="_self">Voir la quête</a>
                    </div>
                </div>""", unsafe_allow_html=True)


def queststeachers():

    st.title("Teachers Dashboard")

    # Load the custom CSS from the file
    with open("assets/styles/quest-styles.css", "r") as f:
        custom_css = f.read()

    # Set the custom CSS for the entire app
    st.markdown(f"<style>{custom_css}</style>", unsafe_allow_html=True)

    st.markdown("""
        <a class='btn-create' href='/?nav=/createquest' target='_self'>Créer une quête</a>
    """, unsafe_allow_html=True)

    # Horizontal card layout
    col1, col2 = st.columns(2)

    for index, item in enumerate(quests_data):
        if index % 2 == 0:
            col = col1
        else:
            col = col2

        with col:
            st.markdown(f"""<div class="card">
                   <div class="empty-star">&#9734;</div> <!-- Empty star icon -->
                    <div class="card-header">
                    {item['title']}
                    </div>
                    <div class="card-body">
                    {item['subTitle']}
                    </div>
                    <div class="card-footer">
                     <div >
                        <svg class="bottom-left-icons" xmlns="http://www.w3.org/2000/svg" width="20" height="20">
                                    <path fill="#FFFFFF" d="m5.2494 8.0688 2.83-2.8269 14.1343 14.15-2.83 2.8269zm4.2363-4.2415 2.828-2.8289 5.6577 5.656-2.828 2.8289zM.9989 12.3147l2.8284-2.8285 5.6569 5.6569-2.8285 2.8284zM1 21h12v2H1z"></path>
                                </svg> 
                                 <svg class="bottom-left-icons" xmlns="http://www.w3.org/2000/svg" width="20" height="20">
                                    <path fill="#FFFFFF" d="M15 1H9v2h6V1zm-4 13h2V8h-2v6zm8.03-6.61 1.42-1.42c-.43-.51-.9-.99-1.41-1.41l-1.42 1.42C16.07 4.74 14.12 4 12 4c-4.97 0-9 4.03-9 9s4.02 9 9 9 9-4.03 9-9c0-2.12-.74-4.07-1.97-5.61zM12 20c-3.87 0-7-3.13-7-7s3.13-7 7-7 7 3.13 7 7-3.13 7-7 7z"></path>
                                </svg> 
                               <span class="bottom-left-text">{item['completionTime']}h</span>
                            </div> 
                     <a class="btn-right" href='/?nav=/questdetailteachers/{item['id']}' target="_self">Voir la quête</a>
                    </div>
                </div>""", unsafe_allow_html=True)


def quest_detail(quest_id):

    # Load the custom CSS from the file
    with open("assets/styles/quest-detail-styles.css", "r") as f:
        custom_css = f.read()

    # Set the custom CSS for the entire app
    st.markdown(f"<style>{custom_css}</style>", unsafe_allow_html=True)

    st.markdown(
        f"""
    <div class="fab-container">
        <div class="fab">
            <span style="font-size: 24px; color: white;">🤖</span>
        </div>
        <div class="dropdown-content">
            <a href='/?nav=/questchat/{quest_id}/summarize' target="_self">Summarize</a>
            <a href='/?nav=/questchat/{quest_id}/translate' target="_self">Translate to french</a>
            <a href='/?nav=/questchat/{quest_id}/explain' target="_self">Explain quest</a>
            <a href='/?nav=/questchat/{quest_id}/simplify' target="_self">Simplify Language</a>
            <a href='/?nav=/questchat/{quest_id}' target="_self">Custom Chat</a>
        </div>
    </div>
    """,
        unsafe_allow_html=True
    )

    quest = None
    for item in quests_data:
        if item['id'] == quest_id:
            quest = item
            presigned_url = item['questLink']
            break

    if quest:
        st.title(quest['title'])

        with open(presigned_url, "r") as file:
            s3_content = file.read()

        st.markdown(s3_content)


def quest_detail_teacher(quest_id):

    # Load the custom CSS from the file
    with open("assets/styles/quest-detail-styles.css", "r") as f:
        custom_css = f.read()

    # Set the custom CSS for the entire app
    st.markdown(f"<style>{custom_css}</style>", unsafe_allow_html=True)

    st.markdown(
        f"""
    <div class="fab-container">
        <div class="fab">
            <span style="font-size: 24px; color: white;">🤖</span>
        </div>
        <div class="dropdown-content">
            <a href='/?nav=/questchat/{quest_id}/quiz' target="_self">Create Quiz</a>
            <a href='/?nav=/questchat/{quest_id}/exercise' target="_self">Create Exercise</a>
            <a href='/?nav=/questchat/{quest_id}/slides' target="_self">Prepare Slides</a>
            <a href='/?nav=/questchat/{quest_id}/guide' target="_self">Study Guide</a>
            <a href='/?nav=/questchat/{quest_id}' target="_self">Custom Chat</a>
        </div>
    </div>
    """,
        unsafe_allow_html=True
    )

    quest = None
    for item in quests_data:
        if item['id'] == quest_id:
            quest = item
            presigned_url = item['questLink']
            break

    
    if quest:
        st.title(quest['title'])
        
        with open(presigned_url, "r") as file:
            s3_content = file.read()

        st.markdown(s3_content)


def questchat(quest_id, predefined_prompt=""):

    # Load the custom CSS from the file
    with open("assets/styles/quest-chat-styles.css", "r") as f:
        custom_css = f.read()

    # Set the custom CSS for the entire app
    st.markdown(f"<style>{custom_css}</style>", unsafe_allow_html=True)

    st.title("💬 Chat with quest")

    for item in quests_data:
        if item['id'] == quest_id:
            quest = item
            presigned_url = item['questLink']
            break

    if quest:
        with open(presigned_url, "r") as file:
            s3_content = file.read()

        prompt_content = f"""
        You are my quest assistant. 
        You will use the following text which is 
        called a quest to answer all my question 
        Here is the quest content: {s3_content}
        if it's clear for you, just answer by: 
        How can I help you with this quest ?
        """

        prompt_content_summarize = f"""
        Summarize the quest content provided below into distinct subjects, 
        highlighting the key information for each. Your summaries should be 
        concise yet comprehensive. Use markdown format for your responses.
        Quest Content: {s3_content}
        """

        prompt_content_translate = f"""
        Translate the quest content provided below into French 
        while ensuring clarity and accuracy. Your translation 
        should effectively convey the original meaning. Use markdown 
        format for your responses.
        Quest Content: {s3_content}
        """

        prompt_content_simplify = f"""
        Rewrite the quest content below in simpler language, 
        targeting beginners. Enhance understanding by providing 
        clear explanations, relatable examples, and straightforward
        definitions. Use markdown format.
        Quest Content: {s3_content}
        """

        prompt_content_explain = f"""
        Explain the quest content to a beginner developer using
        language suitable for a high school student. Use concise 
        explanations, break down complex concepts, and utilize 
        relatable examples. Use markdown format.
        Quest Content: {s3_content}
        """

        prompt_content_create_quiz = f"""
        Develop a comprehensive 10-question quiz that covers essential 
        concepts from the quest. Each question should gauge students' 
        understanding effectively. Include answers. Use markdown format.
        Quest Content: {s3_content}
        """

        prompt_content_create_exercise = f"""
        Design a hands-on exercise that allows students to apply quest concepts.
        Provide step-by-step instructions, guiding them through the process. 
        Include the solution. Use markdown format.
        Quest Content: {s3_content}
        """

        prompt_content_create_slides = f"""
        Create an informative presentation with five slides, 
        delivering a complete understanding of the quest's subject. 
        Utilize concise bullet points to convey crucial information. 
        Use markdown format.
        Quest Content: {s3_content}
        """

        prompt_content_study_guide = f"""
        Compose a comprehensive study guide encompassing all quest concepts. 
        This guide should provide students with a thorough resource for review 
        and learning. Use markdown format.
        Quest Content: {s3_content}
        """

        if "messages" not in st.session_state and predefined_prompt == "summarize":
            st.session_state["messages"] = [
                {"role": "system", "content": "you are a tech expert who can answer any developement or data question with precision"},
                {"role": "user", "content": prompt_content_summarize}]

        elif "messages" not in st.session_state and predefined_prompt == "translate":
            st.session_state["messages"] = [
                {"role": "system", "content": "you are a tech expert who can answer any developement or data question with precision"},
                {"role": "user", "content": prompt_content_translate}]

        elif "messages" not in st.session_state and predefined_prompt == "simplify":
            st.session_state["messages"] = [
                {"role": "system", "content": "you are a tech expert who can answer any developement or data question with precision"},
                {"role": "user", "content": prompt_content_simplify}]

        elif "messages" not in st.session_state and predefined_prompt == "explain":
            st.session_state["messages"] = [
                {"role": "system", "content": "you are a tech expert who can answer any developement or data question with precision"},
                {"role": "user", "content": prompt_content_explain}]

        elif "messages" not in st.session_state and predefined_prompt == "quiz":
            st.session_state["messages"] = [
                {"role": "system", "content": "you are a tech expert who can answer any developement or data question with precision"},
                {"role": "user", "content": prompt_content_create_quiz}]

        elif "messages" not in st.session_state and predefined_prompt == "exercise":
            st.session_state["messages"] = [
                {"role": "system", "content": "you are a tech expert who can answer any developement or data question with precision"},
                {"role": "user", "content": prompt_content_create_exercise}]

        elif "messages" not in st.session_state and predefined_prompt == "slides":
            st.session_state["messages"] = [
                {"role": "system", "content": "you are a tech expert who can answer any developement or data question with precision"},
                {"role": "user", "content": prompt_content_create_slides}]

        elif "messages" not in st.session_state and predefined_prompt == "guide":
            st.session_state["messages"] = [
                {"role": "system", "content": "you are a tech expert who can answer any developement or data question with precision"},
                {"role": "user", "content": prompt_content_study_guide}]

        elif "messages" not in st.session_state:
            st.session_state["messages"] = [
                {"role": "system", "content": "you are a tech expert who can answer any developement or data question with precision"},
                {"role": "user", "content": prompt_content}]

        for msg in st.session_state["messages"]:
            st.chat_message(msg["role"]).write(msg["content"])

        if prompt := st.chat_input():
            # if not openai_api_key:
            #     st.info("Please add your OpenAI API key to continue.")
            #     st.stop()
            with st.spinner("Waiting for a reponse..."):
                st.session_state["messages"].append(
                    {"role": "user", "content": prompt})
                st.chat_message("user").write(prompt)
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo", messages=st.session_state["messages"])
                msg = response.choices[0].message
                st.session_state["messages"].append(msg)
                st.chat_message("assistant").write(msg.content)
        else:
            with st.spinner("Waiting for a reponse..."):
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo", messages=st.session_state["messages"])
                msg = response.choices[0].message
                st.session_state["messages"].append(msg)
                st.chat_message("assistant").write(msg.content)


def createquest():

    # Load the custom CSS from the file
    with open("assets/styles/quest-chat-styles.css", "r") as f:
        custom_css = f.read()

    # Set the custom CSS for the entire app
    st.markdown(f"<style>{custom_css}</style>", unsafe_allow_html=True)

    st.title("💬 Create Quest Chatbot")

    with open("assets/quests/express-quest.txt", "r") as file:
            s3_quest_content = file.read()

    prompt_createt_quest = f"""
        As my quest assistant, your role is to generate new quests based 
        on a given model quest. Here's an example of quest content: {s3_quest_content}. 
        Your task is to craft quests on various topics within the tech or data field upon my request.
        When I provide you with the quest title, your objective is to create in-depth and detailed content. 
        Emphasize thorough explanations and use the provided model quest as a guide. Incorporate relevant 
        examples to enhance comprehension. Your content should be exhaustive and tailored for students' 
        understanding.
        After receiving the quest title, carefully structure the content step by step, ensuring completeness. 
        Utilize markdown format for all your responses.
        """

    if "messages" not in st.session_state:
        st.session_state["messages"] = [
            {"role": "system", "content": "you are a tech expert who can answer any developement or data question with precision"},
            {"role": "user", "content": prompt_createt_quest},
            {"role": "assistant", "content": "I am you quest creator assistant! Give me a title for the quest you want to create."}
        ]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input():
        # if not openai_api_key:
        #     st.info("Please add your OpenAI API key to continue.")
        #     st.stop()
        with st.spinner("Waiting for a reponse..."):
            st.session_state.messages.append(
                {"role": "user", "content": prompt})
            st.chat_message("user").write(prompt)
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", messages=st.session_state.messages)
            msg = response.choices[0].message
            st.session_state.messages.append(msg)
            st.chat_message("assistant").write(msg.content)

# checking the route for specific ids in questdetail and questchat


def extract_integer_from_questdetail(url):
    pattern = r'^/questdetail/(\d+)$'
    match = re.match(pattern, url)
    if match:
        return int(match.group(1))
    else:
        return None


def extract_integer_from_questdetail_teacher(url):
    pattern = r'^/questdetailteachers/(\d+)$'
    match = re.match(pattern, url)
    if match:
        return int(match.group(1))
    else:
        return None


def extract_integer_from_questchat(url):
    pattern = r'^/questchat/(\d+)$'
    match = re.match(pattern, url)
    if match:
        return int(match.group(1))
    else:
        return None


def extract_integer_from_questchat_predefined(url):
    pattern = r'^/questchat/(\d+)/([A-Za-z0-9]+)$'
    match = re.match(pattern, url)
    if match:
        return int(match.group(1)), match.group(2)
    return None


query_params = st.experimental_get_query_params().get("nav")

if query_params:
    matched_integer_detail = extract_integer_from_questdetail(query_params[0])
    matched_integer_detail_teacher = extract_integer_from_questdetail_teacher(
        query_params[0])
    matched_integer_chat = extract_integer_from_questchat(query_params[0])
    matched_predefined_chat = extract_integer_from_questchat_predefined(
        query_params[0])

    if matched_integer_detail:
        quest_detail(matched_integer_detail)
    elif matched_integer_detail_teacher:
        quest_detail_teacher(matched_integer_detail_teacher)
    elif matched_integer_chat:
        questchat(matched_integer_chat)
    elif matched_predefined_chat:
        questchat(matched_predefined_chat[0], matched_predefined_chat[1])

router = init_router()
router.show_route_view()
