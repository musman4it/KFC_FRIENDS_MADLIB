import streamlit as st

# Page configuration
st.set_page_config(page_title="🍗 KFC Friends Feast Planner!", layout="centered")

# Title and header
st.title("🍗 KFC Friends Feast Planner! 🍔")
st.subheader("Plan your delicious feast with friends! 😍")

# Balloons for excitement
st.balloons()

# Friend names input
friend1 = st.text_input("Enter the name of Friend 1 👤")
friend2 = st.text_input("Enter the name of Friend 2 👤")
friend3 = st.text_input("Enter the name of Friend 3 👤")
friend4 = st.text_input("Enter the name of Friend 4 👤")

# Food options and image paths
food_options = {
    "🍔 Mighty Zinger Burger": "images/mighty_zinger.jpg",
    "🍗 5pc Chicken with 2 Soft Drinks": "images/5pc_chicken.jpg",
    "🍟 Fries": "images/fries.jpg",
    "🍗 16pcs Chicken Bucket with 4 Soft Drinks": "images/16pcs_bucket.jpg"
}

# Food selection for each friend
st.markdown("### 🍽️ Select food for each friend:")

friend1_food = st.selectbox(f"What does {friend1} want to eat?", list(food_options.keys()), key="f1")
friend2_food = st.selectbox(f"What does {friend2} want to eat?", list(food_options.keys()), key="f2")
friend3_food = st.selectbox(f"What does {friend3} want to eat?", list(food_options.keys()), key="f3")
friend4_food = st.selectbox(f"What does {friend4} want to eat?", list(food_options.keys()), key="f4")

# Generate story button
if st.button("Generate Our KFC Story"):
    st.markdown("## 🍗 Our KFC Plan 🍗")
    
    st.write(f"One fine day, **{friend1}**, **{friend2}**, **{friend3}**, and **{friend4}** made an exciting plan to visit KFC randomly! 🎉")
    st.write(f"They were all super hungry and excited to order their favorite meals.")

    # Display choices with images
    st.markdown(f"### {friend1}'s Choice: {friend1_food}")
    st.image(food_options[friend1_food], caption=friend1_food, use_container_width=True)

    st.markdown(f"### {friend2}'s Choice: {friend2_food}")
    st.image(food_options[friend2_food], caption=friend2_food, use_container_width=True)

    st.markdown(f"### {friend3}'s Choice: {friend3_food}")
    st.image(food_options[friend3_food], caption=friend3_food, use_container_width=True)

    st.markdown(f"### {friend4}'s Choice: {friend4_food}")
    st.image(food_options[friend4_food], caption=friend4_food, use_container_width=True)

    # Final message
    st.success("It was an awesome feast! They laughed, ate, and had the best time together! ❤️")
    st.snow()  # Optional: Snow effect

# Footer
st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
