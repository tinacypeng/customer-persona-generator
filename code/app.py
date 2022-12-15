# Imports
import pandas as pd
import random
import streamlit as st
import streamlit.components.v1 as components
import python_avatars as pa

### Avatar Generator
def avatar_generator(ava_gender, i):
    # hair style
    female_hair_type = [
        pa.HairType.STRAIGHT_STRAND, 
        pa.HairType.BOB,
        pa.HairType.LONG_NOT_TOO_LONG,
        pa.HairType.BRIDE,
        pa.HairType.CURLY_2,
        pa.HairType.MIA_WALLACE,
        pa.HairType.STRAIGHT_1,
        pa.HairType.STRAIGHT_2
        ]
    male_hair_type = [
        pa.HairType.SHAGGY, 
        pa.HairType.SHORT_FLAT,
        pa.HairType.CAESAR,
        pa.HairType.CAESAR_SIDE_PART,
        pa.HairType.SHORT_WAVED,
        pa.HairType.POMPADOUR,
        pa.HairType.ELVIS,
        pa.HairType.BUZZCUT
        ]

    # clothing color
    clothing_color = [
        "#E5CB93", "#A9DBEA", "#DBD2F4", "#FF8B71", "#878ECD", "#046582",
        "#DAD8D7", "#DAD8D7", "#C0D8C0", "#DD4A48", "#FEA82F", "#FF6701"]

    # clothing style
    clothing_style = [
        pa.ClothingType.SHIRT_SCOOP_NECK,
        pa.ClothingType.BLAZER_SWEATER,
        pa.ClothingType.COLLAR_SWEATER,
        pa.ClothingType.HOODIE,
        pa.ClothingType.SHIRT_CREW_NECK
        ]

    # hair color
    hair_color = [
        "#6B3307", "#000000", "#C4942D", "#B05A08", "#3F4E4F", "#A27B5C",
        "#A19882", "#555555", "#7F7C82", "#FEA82F"]

    if ava_gender == 'female':
        my_avatar = pa.Avatar(
            style = pa.AvatarStyle.CIRCLE,
            background_color = "#F4F9F9",
            top = random.choice(female_hair_type),
            eyebrows = pa.EyebrowType.DEFAULT_NATURAL,
            eyes = pa.EyeType.DEFAULT,
            nose = pa.NoseType.DEFAULT,
            mouth = pa.MouthType.SMILE,
            facial_hair = pa.FacialHairType.NONE,
            skin_color = "#FBD9BF",
            hair_color = random.choice(hair_color),
            accessory = pa.AccessoryType.NONE,
            clothing = random.choice(clothing_style),
            clothing_color = random.choice(clothing_color)
        )
    else:
        my_avatar = pa.Avatar(
            style = pa.AvatarStyle.CIRCLE,
            background_color="#F4F9F9",
            top = random.choice(male_hair_type),
            eyebrows = pa.EyebrowType.DEFAULT_NATURAL,
            eyes = pa.EyeType.DEFAULT,
            nose = pa.NoseType.DEFAULT,
            mouth = pa.MouthType.SMILE,
            facial_hair = pa.FacialHairType.NONE,
            skin_color = "#FBD9BF",
            hair_color = random.choice(hair_color),
            accessory = pa.AccessoryType.NONE,
            clothing = random.choice(clothing_style),
            clothing_color = random.choice(clothing_color)
        )

        # Save to a file
    image_svg = my_avatar.render("../pics/group_%s_persona_image.svg" %(i))
    image_svg = image_svg.replace("264px", "100%")
    image_svg = image_svg.replace("280px", "100%")

    return image_svg

### Web Page Structure
# Main Title
st.header("°◌ Customer Persona ◌°")

# Customer info by group
summary = pd.read_csv('../data/summary_result.csv')
group = summary.group
group_pop = summary.group_size
spend_level = summary.spending_level

# Layouts
# Tabs
tab1, tab2, tab3, tab4, tab_sum = st.tabs(["Group " + i for i in group]+['Summary'])

# summary tab
with tab_sum:
    col1, col2 = st.columns(int(len(summary)/2))
    col3, col4 = st.columns(int(len(summary)/2))
    cols = [col1, col2, col3, col4]
    for i, col in enumerate(cols[:int(len(summary)/2)]):
        with col:
            product_preference = summary['pro_preference'][i].replace('[', '').replace(']', '').replace(' ', '').replace("'", '').split(',')
            if i % 2 == 1:
                st.info(f'''
                        **Group {group[i]}**
                        - Group size: **{str(round(group_pop[i]*100))+'%'}**\n
                        - Annual income: **${round(summary.income_q1[i]/1000)},000 ~ {round(summary.income_q3[i]/1000)},000**\n
                        - Spending amount: **${int(summary.spending_q1[i])} ~ {int(summary.spending_q3[i])}**\n
                        - Age: **{int(summary.age_q1[i])} ~ {int(summary.age_q3[i])}**\n
                        - Marital status: **{int(summary.married_pr[i]*100)}% are married**\n
                        - Family size: **{int(summary.num_family_member_q1[i])+1} ~ {int(summary.num_family_member_q3[i])+1}**\n
                        - Product preference: **{', '.join(product_preference)}**
                        '''
                        )
            else:
                st.warning(f'''
                        **Group {group[i]}**
                        - Group size: **{str(round(group_pop[i]*100))+'%'}**\n
                        - Annual income: **${round(summary.income_q1[i]/1000)},000 ~ {round(summary.income_q3[i]/1000)},000**\n
                        - Spending amount: **${int(summary.spending_q1[i])} ~ {int(summary.spending_q3[i])}**\n
                        - Age: **{int(summary.age_q1[i])} ~ {int(summary.age_q3[i])}**\n
                        - Marital status: **{int(summary.married_pr[i]*100)}% are married**\n
                        - Family size: **{int(summary.num_family_member_q1[i])+1} ~ {int(summary.num_family_member_q3[i])+1}**\n
                        - Product preference: **{', '.join(product_preference)}**
                        ''')
    for i, col in enumerate(cols[int(len(summary)/2):]):
        n = i + int(len(summary)/2)
        with col:
            product_preference = summary['pro_preference'][n].replace('[', '').replace(']', '').replace(' ', '').replace("'", '').split(',')
            if i % 2 == 0:
                    st.info(f'''
                        **Group {group[n]}**
                        - Group size: **{str(round(group_pop[n]*100))+'%'}**\n
                        - Annual income: **${round(summary.income_q1[n]/1000)},000 ~ {round(summary.income_q3[n]/1000)},000**\n
                        - Spending amount: **${int(summary.spending_q1[n])} ~ {int(summary.spending_q3[n])}**\n
                        - Age: **{int(summary.age_q1[n])} ~ {int(summary.age_q3[n])}**\n
                        - Marital status: **{int(summary.married_pr[n]*100)}% are married**\n
                        - Family size: **{int(summary.num_family_member_q1[n])+1} ~ {int(summary.num_family_member_q3[n])+1}**\n
                        - Product preference: **{', '.join(product_preference)}**
                        ''')
            else:
                st.warning(f'''
                        **Group {group[n]}**
                        - Group size: **{str(round(group_pop[n]*100))+'%'}**\n
                        - Annual income: **${round(summary.income_q1[n]/1000)},000 ~ {round(summary.income_q3[n]/1000)},000**\n
                        - Spending amount: **${int(summary.spending_q1[n])} ~ {int(summary.spending_q3[n])}**\n
                        - Age: **{int(summary.age_q1[n])} ~ {int(summary.age_q3[n])}**\n
                        - Marital status: **{int(summary.married_pr[n]*100)}% are married**\n
                        - Family size: **{int(summary.num_family_member_q1[n])+1} ~ {int(summary.num_family_member_q3[n])+1}**\n
                        - Product preference: **{', '.join(product_preference)}**
                        ''')


# other tabs
tabs = [tab1, tab2, tab3, tab4]
for i, tab in enumerate(tabs):
    with tab:
        st.code("")
        col1, col2, col3, col4, col5 = st.columns([2.5, 1, 0.3, 1, 1.2])
        with col2:
            # Gender
            gender = random.choice(['female', 'male'])
            st.text("GENDER")
            st.subheader(gender.title())
        
        with col1:
            # Name
            name_df = pd.read_csv('../data/name_list.csv')
            ava_name = random.choice(name_df[gender].to_list()) + ' ' + random.choice(name_df['last'].to_list())
            st.text("NAME")
            st.subheader(ava_name)
        
        with col4:
            # Age
            st.text("AGE")
            st.subheader("%i" %(
                random.randint(int(summary.age_q1[i]), int(summary.age_q3[i]))-3))

        with col5:
            # Group
            st.text("GROUP SIZE")
            st.subheader(f"{round(group_pop[i]*100)}%")

        st.code("")
        col1, col2, col3 = st.columns([1, 0.35 ,2])
        with col1:
            # Avatar image
            components.html(avatar_generator(gender, group[i]), height = 220, width = 200)

        with col3:
            # Customer profile
            st.text("CUSTOMER PROFILE")
            c = st.container()
            marital_status = random.choice([
                summary.not_live_alone_q1[i], 
                summary.not_live_alone_q3[i]])
            n_kid = random.randint(
                int(summary.num_child_q1[i]),
                int(summary.num_child_q3[i]))
            if marital_status == 'Single':
                n_fm = n_kid + 1
            else:
                n_fm = n_kid + 2
            c.write('''\n
                    - Annual income: **$%i,000**\n
                    - Spending level: **%s**\n
                    - Marital status: **%s**\n
                    - Number of family member: **%i**\n
                    - Number of kids: **%i**
                    ''' %(
                        random.randrange(
                            round(summary.income_q1[i]/1000), 
                            round(summary.income_q3[i]/1000)), 
                        spend_level[i], 
                        marital_status, 
                        n_fm, 
                        n_kid))
        st.code("")
        st.text("PRODUCT PREFERENCE")
        product_preference = summary['pro_preference'][i].replace('[', '').replace(']', '').replace(' ', '').replace("'", '').split(',')
        col1, col2, col3 = st.columns(3)
        with col1:
            if 'Wine' in product_preference:
                st.warning("🍷 Wine")
            else:
                st.code("🍷 Wine")
        with col2:
            if 'Fruits' in product_preference:
                st.warning("🍋 Fruits")
            else:
                st.code("🍋 Fruits")
        with col3:
            if 'Meats' in product_preference:
                st.warning("🥩 Meats")
            else:
                st.code("🥩 Meats")
        col4, col5, col6 = st.columns(3)
        with col4:
            if 'Seafood' in product_preference:
                st.warning("🐟 Seafood")
            else:
                st.code("🐟 Seafood")
        with col5:
            if 'Sweets' in product_preference:
                st.warning("🍰 Sweets")
            else:
                st.code("🍰 Sweets")
        with col6:
            #if 'deal' in product_preference:
                #st.warning("💎 Gold ➞ 🎊 on sale")
            if 'Gold' in product_preference:
                st.warning("💎 Gold")
            else:
                st.code("💎 Gold")
        col7, col8, col9 = st.columns(3)
        with col7:
            if 'On-sale' in product_preference:
                st.warning("🎊 On-sale Products")
            else:
                st.code("🎊 On-sale Products")
        st.code("")



    









   