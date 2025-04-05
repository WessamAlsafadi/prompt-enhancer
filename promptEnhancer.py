# import streamlit as st
# from groq import Groq

# # API Key
# GROQ_API_KEY = "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"

# # Initialize Client
# groq_client = Groq(api_key=GROQ_API_KEY)

# st.title("⚡ Prompt Enhancer Tool")

# prompt_type = st.selectbox(
#     "What are you using the prompt for?",
#     ["", "🖼️ Image Generation", "🎥 Video Prompting", "💬 General Info / Chat", "🛍️ E-commerce Product Image"]
# )

# user_prompt = ""
# ecom_fields = {}

# # E-commerce Dynamic Form
# if prompt_type == "🛍️ E-commerce Product Image":
#     st.subheader("🧱 Product Core")
#     ecom_fields["product"] = st.text_input("What is the product?")
#     ecom_fields["materials"] = st.multiselect("Materials", ["Glass", "Metal", "Fabric", "Plastic", "Leather"])
#     ecom_fields["materials_expand"] = st.text_input("Other materials:")
#     ecom_fields["colors"] = st.text_input("Primary colors (hex or names)")
#     ecom_fields["reference"] = st.radio("Do you have a reference image?", ["Yes", "No"])
#     ecom_fields["reference_expand"] = st.text_input("Describe reference image")
#     ecom_fields["rotation"] = st.selectbox("Product rotation/tilt", ["Static", "Slight Rotation", "Dynamic Twist", "Hovering with Motion Trail"])

#     st.subheader("🌍 Background & Environment")
#     ecom_fields["background"] = st.text_input("Background setting (e.g. Tokyo city)")
#     ecom_fields["bg_elements"] = st.multiselect("Background elements", ["Greenery", "Floating Platforms", "Glowing Lines", "Water", "Creatures", "Architecture"])
#     ecom_fields["bg_colors"] = st.text_input("Background colors")
#     ecom_fields["time_of_day"] = st.selectbox("Time of day", ["Morning", "1–2 PM", "Golden Hour", "Dusk", "Night"])
#     ecom_fields["vibe"] = st.selectbox("Environment vibe", ["Peaceful", "Sacred", "Cinematic", "Intense", "Mystical"])
#     ecom_fields["env_effects"] = st.multiselect("Environmental Effects", ["Reflections", "Dust", "Auras", "Light Trails"])

#     st.subheader("💡 Lighting & Camera")
#     ecom_fields["lighting"] = st.multiselect("Lighting setup", ["Ambient", "Overhead", "Side Glow", "Backlight", "Dynamic Pulses"])
#     ecom_fields["light_feel"] = st.selectbox("Lighting feel", ["Cinematic", "Soft Natural", "Harsh Contrast", "Ethereal"])
#     ecom_fields["camera"] = st.selectbox("Camera angle", ["Eye-level", "Low-angle", "Wide", "Close-up", "Top-down"])
#     ecom_fields["realism"] = st.slider("Realism Level (%)", 0, 100, 100)

#     st.subheader("🧊 Texture & Detail Focus")
#     ecom_fields["textures"] = st.multiselect("Material textures", ["Brushed Metal", "Glowing Edges", "Leather Grain"])
#     ecom_fields["shadows"] = st.multiselect("Reflections/Shadows", ["Sharp Shadows", "Soft Glow", "Mirror Floor", "Natural Surface"])

#     st.subheader("🧍 Composition & Branding")
#     ecom_fields["collection"] = st.radio("Product display", ["Solo", "Collection"])
#     ecom_fields["text_space"] = st.radio("Leave space for text?", ["Yes", "No"])
#     ecom_fields["fade_behind"] = st.radio("Fade/blur background behind text?", ["Yes", "No"])
#     ecom_fields["logo"] = st.selectbox("Logo placement", ["On Product", "Floating", "Background"])
#     ecom_fields["symbol"] = st.radio("Embed brand symbol subtly?", ["Yes", "No"])

#     st.subheader("🎯 Purpose, Feel, CTA")
#     ecom_fields["platform"] = st.selectbox("Platform", ["Instagram Post", "Story", "Facebook Ad", "Banner", "Print"])
#     ecom_fields["goal"] = st.selectbox("Image Goal", ["Branding", "Showcase", "Ad / Conversion", "Creative"])
#     ecom_fields["emotion"] = st.multiselect("Emotion", ["Luxury", "Rebellion", "Peace", "Confidence", "Curiosity"])
#     ecom_fields["branding"] = st.text_input("Brand messaging (e.g. Minimalism, Innovation)")
#     ecom_fields["narrative"] = st.text_input("Narrative moment?")
#     ecom_fields["cta"] = st.selectbox("CTA", ["Shop Now", "Try It Today", "Discover More", "Join the Movement", "No CTA"])

# else:
#     user_prompt = st.text_area("📝 Enter your raw idea or prompt:", height=150)

# # System Prompts
# image_system = """Role & Purpose  
# You are a Prompt Enhancer specialized in optimizing text-to-image prompts for AI models such as Midjourney, Flux, Ideogram, DALL·E, and other generative image systems. Your purpose is to take simple, vague, or underdeveloped user inputs and transform them into highly detailed, structured prompts that maximize clarity, artistic direction, and style specificity without being unnecessarily verbose.

# Focus on enhancing prompts using precise descriptions of the scene, subject details, setting, lighting, mood, and composition while maintaining conciseness and avoiding unnecessary complexity. Always prioritize delivering prompts that are visually compelling, technically refined, and well-formatted for AI interpretation. Your outputs should reflect best practices in visual prompt engineering, ensuring optimal results while adapting to different artistic styles and rendering techniques.

# Prompting Tips & Tricks for AI Image Generation  
# 1. Keep It Concise & Descriptive  
# Think of your prompt as a snapshot. Use clear, direct phrasing.  
# ❌ "Show me a picture of blooming California poppies, make them bright orange, and drawn in colored pencils."  
# ✅ "Colored pencil illustration of bright orange California poppies."

# 2. Use Strong, Specific Words  
# Instead of “big,” use “towering,” “gigantic,” or “colossal.” Descriptive words drive better image accuracy.

# 3. Use Specific Quantities  
# “A group of cats” → “Three black cats sitting on a fence.”

# 4. Focus on What You Want (Not What You Don’t)  
# Avoid negation like “without cake.” Instead, describe what should be in the image.

# 5. Balance Detail with Clarity  
# Be specific about mood, lighting, subject details, and style — without overloading the sentence.

# Prompt Structure:
# - **Scene**: Core action or setting (e.g., "A lone warrior in a snowy forest")
# - **Subject Details**: Appearance, outfit, expressions, accessories
# - **Setting Details**: Environment, lighting, atmosphere, color palette
# - **Style Details**: Medium, camera angle, texture, artist influence

# Example Prompt – Cyberpunk Warrior  
# "A cyberpunk warrior stands on a rain-soaked rooftop, neon lights reflecting off his metallic armor. He holds a glowing katana, face partially shadowed under a hood. Electric-blue smoke rises behind him. Cinematic lighting, wide shot, high-detail digital art, Blade Runner-inspired, 8K resolution."

# Respond only with the enhanced prompt. Do not include commentary or suggestions.
# """
# video_system = """Role & Purpose  
# You are a Prompt Enhancer specialized in optimizing text-to-video prompts for AI models such as Sora, Runway, Pika, and other generative video systems. Your purpose is to transform vague or underdeveloped user inputs into cinematic, structured prompts that provide clear guidance on scene composition, pacing, motion, mood, and visual style. Focus on expanding ideas into dynamic sequences that describe camera angles, character actions, environment, lighting, and emotional tone. Avoid being too verbose — be intentional and direct while preserving visual richness. Your prompts should reflect best practices in video storytelling and shot direction, making them easy for generative AI to interpret and animate.

# Prompting Tips for Video Generation  
# 1. Think in Shots or Scenes  
# Describe each major shot clearly — what’s visible, how it moves, and how it feels.  
# Example: "A close-up of a woman slowly opening her eyes, soft morning light filtering through a window."  

# 2. Use Action Verbs  
# Keep things moving. Instead of "a boy at a train station," write "a young boy stands alone on a quiet train platform as the wind rustles his coat."  

# 3. Include Camera Movement  
# Pan, zoom, handheld, dolly, slow-motion — define how the scene unfolds.  
# Example: "Wide-angle dolly shot following a man walking through a foggy forest."  

# 4. Emphasize Mood + Atmosphere  
# Mention lighting, weather, emotion. These shape the feel of the video.  
# Example: "Golden hour sunset bathes the rooftops in soft orange light as birds fly past."  

# 5. Structure Matters  
# You can break longer scenes into 2–3 shots for better control. Think of it like a mini storyboard.  

# Prompt Structure:  
# - **Scene Overview:** Core idea or narrative  
# - **Subject & Action:** What’s happening and to whom  
# - **Environment & Atmosphere:** Where it’s happening and how it feels  
# - **Camera & Style:** How it’s shot and rendered  

# Example Prompt – Cyberpunk Alley  
# "A cyberpunk city alleyway at night. Rain pours as a hooded figure runs past neon-lit walls. The camera follows in a handheld tracking shot, capturing reflections on the wet pavement. Thunder rumbles as the figure pauses under a flickering sign, catching their breath. Shot in cinematic style with dramatic contrast, moody lighting, and slow-motion elements."

# Respond only with the enhanced prompt. Do not add commentary or extra explanation.
# """
# general_system = """Role & Purpose  
# You are a Prompt Optimizer for language-based AI models like GPT-4. Your task is to take vague, unclear, or underdeveloped prompts and rewrite them into clear, structured, and effective instructions. Your optimized prompts should make it easier for AI models to understand user intent and deliver useful, relevant, and high-quality responses.

# Your enhanced prompts should improve specificity, remove ambiguity, and maintain an appropriate tone for the user's goal — whether that’s writing, explaining, brainstorming, analyzing, or solving a task.

# Optimization Guidelines:
# 1. Clarify the Task  
# If it’s unclear what the user wants, infer and make it precise.  
# ❌ "Tell me something cool"  
# ✅ "List five fascinating facts about space exploration for a science blog."

# 2. Use Clear Instructions  
# Include context, desired tone, and output format.  
# ❌ "Explain AI"  
# ✅ "Write a beginner-friendly explanation of how AI models like GPT-4 work, using simple language and real-world examples."

# 3. Be Outcome-Oriented  
# Structure the prompt around the intended result.  
# Examples:
# - For writing → "Write a persuasive LinkedIn post for marketers about using AI tools."
# - For solving → "Solve this logic puzzle and explain the reasoning behind the answer."
# - For analysis → "Analyze this customer review and summarize the user sentiment."

# 4. Be Format-Specific if Needed  
# If you expect bullet points, numbered lists, tables, etc., include it in the prompt.

# 5. Maintain Professionalism  
# Even if informal, the output should still be grammatically correct, direct, and logical.

# Respond only with the enhanced prompt. Do not add explanations or extra commentary.
# """

# ecommerce_system = """You are an expert in cinematic product imagery. Based on the detailed creative brief, write a stunning and clean prompt for AI image generation (like Midjourney or DALL-E). Focus on describing the product appearance, background, lighting, camera style, emotion, and branding clearly. Return only the final prompt."""

# system_prompt_map = {
#     "🖼️ Image Generation": image_system,
#     "🎥 Video Prompting": video_system,
#     "💬 General Info / Chat": general_system,
#     "🛍️ E-commerce Product Image": ecommerce_system
# }

# # Helper: format E-commerce prompt
# def build_ecommerce_text(data):
#     lines = []
#     for k, v in data.items():
#         val = ", ".join(v) if isinstance(v, list) else v
#         lines.append(f"{k.replace('_', ' ').capitalize()}: {val}")
#     return "\n".join(lines)

# # Response Generator
# def generate_response(user_input, system_prompt):
#     messages = [
#         {"role": "system", "content": system_prompt},
#         {"role": "user", "content": user_input}
#     ]
#     completion = groq_client.chat.completions.create(
#         model="llama3-70b-8192",
#         messages=messages,
#         temperature=0.5
#     )
#     return completion.choices[0].message.content

# # Button
# if st.button("✨ Enhance Prompt"):
#     if not prompt_type:
#         st.warning("Please select a prompt type.")
#     elif prompt_type == "🛍️ E-commerce Product Image":
#         structured_input = build_ecommerce_text(ecom_fields)
#         result = generate_response(structured_input, ecommerce_system)
#     elif not user_prompt.strip():
#         st.warning("Please enter a prompt.")
#     else:
#         system_prompt = system_prompt_map[prompt_type]
#         result = generate_response(user_prompt, system_prompt)

#     if 'result' in locals():
#         st.subheader("🔧 Enhanced Prompt")
#         st.code(result, language="markdown")

#         col1, col2, col3 = st.columns(3)
#         with col1:
#             st.code(f"/imagine prompt: {result} --v 5 --style raw")
#         with col2:
#             st.code(result)
#         with col3:
#             st.download_button("💾 Download Prompt", result, file_name="prompt.txt")



# ###################################################################################################333
# #############################################################################################3
# ##################################################################################3
# ####################################################################################

import streamlit as st
from groq import Groq

# API Key
GROQ_API_KEY = "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"

# Initialize Client
groq_client = Groq(api_key=GROQ_API_KEY)

# Sidebar Layout
st.sidebar.title("⚡ Prompt Enhancer Tool")
prompt_type = st.sidebar.selectbox(
    "What are you using the prompt for?",
    ["", "🖼️ Image Generation", "🎥 Video Prompting", "💬 General Info / Chat", "🛍️ E-commerce Product Image"]
)

video_mode = None
if prompt_type == "🎥 Video Prompting":
    video_mode = st.sidebar.radio(
        "Choose your video prompt type:",
        ["🎞️ Cinematic Scene Generation", "📝 Script-Based Tools (InVideo, Pictory, etc.)"]
    )

# Content Area
st.title("Enhanced Prompt Generator")

user_prompt = ""
ecom_fields = {}

# History Storage
if "history" not in st.session_state:
    st.session_state.history = []

# Input Fields
if prompt_type == "🛍️ E-commerce Product Image":
    st.header("📦 E-commerce Prompt Builder")
    ecom_fields["product"] = st.text_input("What is the product?")
    ecom_fields["materials"] = st.multiselect("Materials", ["Glass", "Metal", "Fabric", "Plastic", "Leather"])
    ecom_fields["materials_expand"] = st.text_input("Other materials:")
    ecom_fields["colors"] = st.text_input("Primary colors (hex or names)")
    ecom_fields["reference"] = st.radio("Do you have a reference image?", ["Yes", "No"])
    ecom_fields["reference_expand"] = st.text_input("Describe reference image")
    ecom_fields["rotation"] = st.selectbox("Product rotation/tilt", ["Static", "Slight Rotation", "Dynamic Twist", "Hovering with Motion Trail"])

    st.subheader("🌍 Background & Environment")
    ecom_fields["background"] = st.text_input("Background setting (e.g. Tokyo city)")
    ecom_fields["bg_elements"] = st.multiselect("Background elements", ["Greenery", "Floating Platforms", "Glowing Lines", "Water", "Creatures", "Architecture"])
    ecom_fields["bg_colors"] = st.text_input("Background colors")
    ecom_fields["time_of_day"] = st.selectbox("Time of day", ["Morning", "1–2 PM", "Golden Hour", "Dusk", "Night"])
    ecom_fields["vibe"] = st.selectbox("Environment vibe", ["Peaceful", "Sacred", "Cinematic", "Intense", "Mystical"])
    ecom_fields["env_effects"] = st.multiselect("Environmental Effects", ["Reflections", "Dust", "Auras", "Light Trails"])

    st.subheader("💡 Lighting & Camera")
    ecom_fields["lighting"] = st.multiselect("Lighting setup", ["Ambient", "Overhead", "Side Glow", "Backlight", "Dynamic Pulses"])
    ecom_fields["light_feel"] = st.selectbox("Lighting feel", ["Cinematic", "Soft Natural", "Harsh Contrast", "Ethereal"])
    ecom_fields["camera"] = st.selectbox("Camera angle", ["Eye-level", "Low-angle", "Wide", "Close-up", "Top-down"])
    ecom_fields["realism"] = st.slider("Realism Level (%)", 0, 100, 100)

    st.subheader("🧊 Texture & Detail Focus")
    ecom_fields["textures"] = st.multiselect("Material textures", ["Brushed Metal", "Glowing Edges", "Leather Grain"])
    ecom_fields["shadows"] = st.multiselect("Reflections/Shadows", ["Sharp Shadows", "Soft Glow", "Mirror Floor", "Natural Surface"])

    st.subheader("🧍 Composition & Branding")
    ecom_fields["collection"] = st.radio("Product display", ["Solo", "Collection"])
    ecom_fields["text_space"] = st.radio("Leave space for text?", ["Yes", "No"])
    ecom_fields["fade_behind"] = st.radio("Fade/blur background behind text?", ["Yes", "No"])
    ecom_fields["logo"] = st.selectbox("Logo placement", ["On Product", "Floating", "Background"])
    ecom_fields["symbol"] = st.radio("Embed brand symbol subtly?", ["Yes", "No"])

    st.subheader("🎯 Purpose, Feel, CTA")
    ecom_fields["platform"] = st.selectbox("Platform", ["Instagram Post", "Story", "Facebook Ad", "Banner", "Print"])
    ecom_fields["goal"] = st.selectbox("Image Goal", ["Branding", "Showcase", "Ad / Conversion", "Creative"])
    ecom_fields["emotion"] = st.multiselect("Emotion", ["Luxury", "Rebellion", "Peace", "Confidence", "Curiosity"])
    ecom_fields["branding"] = st.text_input("Brand messaging (e.g. Minimalism, Innovation)")
    ecom_fields["narrative"] = st.text_input("Narrative moment?")
    ecom_fields["cta"] = st.selectbox("CTA", ["Shop Now", "Try It Today", "Discover More", "Join the Movement", "No CTA"])
else:
    user_prompt = st.text_area("📝 Enter your raw idea or prompt:", height=150)

# Prompt Builders
def build_ecommerce_text(data):
    lines = []
    for k, v in data.items():
        val = ", ".join(v) if isinstance(v, list) else v
        lines.append(f"{k.replace('_', ' ').capitalize()}: {val}")
    return "\n".join(lines)

# System Prompts
image_system = """🎯 Role & Objective
You are a world-class Prompt Enhancer trained to rewrite simple or vague inputs into masterfully crafted prompts for AI image generators like Midjourney, Ideogram, DALL·E, and Luma. You act like a visual director + art strategist, extracting visual depth, structure, and aesthetic quality from any idea.

🧠 Your Method:
• Prioritize scene clarity, character detail, lighting, textures, and emotional tone.
• Incorporate style, realism, and technique: camera lens, art medium, composition, aesthetic inspiration.
• Avoid verbosity. Be elegant, precise, and cinematic in your language.

📸 Prompt Framework:
- Scene: Core subject and action
- Subject Details: Expression, texture, pose, accessories
- Environment: Location, time, lighting, weather, shadows
- Style: Art form, camera, realism level, references (e.g. Blade Runner, Studio Ghibli)

✅ Example Prompt:
"A samurai stands in a misty bamboo forest at dawn, light breaking through the trees. His armor reflects soft sunlight, and falling petals swirl around. Cinematic composition, 50mm lens, hyper-realistic, inspired by Ghost of Tsushima."

⚠️ Reply ONLY with the enhanced prompt. No explanations, no intros, no commentary.
"""
video_system = """🎬 Role & Objective  
You are a cinematic prompt enhancer trained to convert user input into video-ready scenes for models like Sora, Luma Dream Machine, Pika, and Runway. You think like a film director — focusing on how the scene feels, moves, and is shot.

📹 Prompt Focus:
• Frame the scene with camera logic: pan, dolly, aerial, handheld.
• Show character actions and reactions.
• Use lighting, time of day, and emotion to shape mood.
• Write like a visual storyteller — poetic, efficient, and scene-anchored.

🎞️ Prompt Format:
- Scene Overview: What’s happening
- Subject: Who’s on screen and what they’re doing
- Atmosphere: Setting, lighting, mood, style
- Camera: How it's filmed (dolly, zoom, slow motion, etc.)

✅ Example Prompt:
"A man stands at the edge of a canyon at sunset. Wind ripples his coat as the camera slowly pans around him. Golden light spills across the rocks. Tense atmosphere, epic scale, cinematic tone, 24fps slow motion, drone-style orbit."

⚠️ Return ONLY the enhanced prompt. No commentary or intro text.
"""

video_script_system = """🎯 Role & Objective  
You are a Video Script Writer specializing in marketing, ads, educational explainers, and product storytelling. You take simple ideas and transform them into engaging, concise, and structured scripts suitable for platforms like InVideo, Pictory, Lumen5, and Synthesia.

🧠 Script Focus:
- Hook → Problem → Solution → CTA
- Clear, simple, emotionally resonant tone
- Optionally include narration, on-screen text, or visuals

✅ Example Prompt:
"Write a 45-second product explainer script for a hydration water bottle, targeting fitness enthusiasts. Highlight benefits, brand tone (energizing), and include a call to action at the end."

⚠️ Return ONLY the optimized script prompt. No explanations or intros.
"""
general_system = """🧠 Role & Objective
You are a prompt refiner built to translate vague or poorly formed user questions into crystal-clear instructions for large language models like GPT-4. You act like a strategist and translator — taking chaotic thoughts and turning them into purpose-driven prompts with razor clarity.

📌 Optimization Focus:
• Identify intent → Clarify goal
• Remove fluff → Add structure
• Align with tone → Define output style

🧭 Prompt Format Guidelines:
- Task: What the AI should do
- Output: Expected format (list, essay, analysis, etc.)
- Tone: Casual, professional, playful, etc.
- Context: Who or what the answer is for

✅ Example:
❌ "Tell me about dreams"
✅ "Write a short, friendly blog post for teens explaining the science of dreams and why they matter."

⚠️ Reply ONLY with the rewritten prompt. Do not include any explanation, intro, or commentary.
"""
ecommerce_system = "You are an expert in cinematic product image prompting. Based on the provided fields, write a clean, detailed prompt for Midjourney or DALL·E. Focus on product, background, lighting, camera, mood, branding. Reply only with the enhanced prompt."

# Prompt Generator
def generate_response(user_input, system_prompt):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input}
    ]
    completion = groq_client.chat.completions.create(
        model="llama3-70b-8192",
        messages=messages,
        temperature=0.5
    )
    return completion.choices[0].message.content

# Enhance Prompt
if st.button("✨ Enhance Prompt"):
    if not prompt_type:
        st.warning("Please select a prompt type.")
    elif prompt_type == "🛍️ E-commerce Product Image":
        structured_input = build_ecommerce_text(ecom_fields)
        result = generate_response(structured_input, ecommerce_system)
    elif not user_prompt.strip():
        st.warning("Please enter a prompt.")
    else:
        if prompt_type == "🎥 Video Prompting":
            selected_system = video_script_system if video_mode == "📝 Script-Based Tools (InVideo, Pictory, etc.)" else video_system
        elif prompt_type == "🖼️ Image Generation":
            selected_system = image_system
        else:
            selected_system = general_system

        result = generate_response(user_prompt, selected_system)

    if 'result' in locals():
        st.session_state.history.append(result)

        st.subheader("🔧 Enhanced Prompt")
        st.code(result, language="markdown")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.code(f"/imagine prompt: {result} --v 5 --style raw")
        with col2:
            st.code(result)
        with col3:
            st.download_button("💾 Download Prompt", result, file_name="prompt.txt")

        st.markdown("### 🧠 Prompt Preview (Mockup)")
        st.image("https://placehold.co/600x300?text=Sample+AI+Render+Preview", caption="This is a simulated preview for the enhanced prompt.")

# Show Prompt History
if st.session_state.history:
    st.markdown("## 📜 Prompt History")
    for i, item in enumerate(reversed(st.session_state.history[-5:]), 1):
        st.markdown(f"**{i}.** `{item}`")
