import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np

st.set_page_config(page_title="AirBnb Data Visualization", page_icon="airbnb.png", layout="wide", initial_sidebar_state="expanded")

# Display title and text
st.title("Week 1 - Data and visualization")
st.markdown("Here we can see the dataframe created during this week project.")

# Read dataframe
dataframe = pd.read_csv(
    "WK1_Airbnb_Amsterdam_listings_proj_solution.csv",
    names=[
        "Airbnb Listing ID",
        "Price",
        "Latitude",
        "Longitude",
        "Meters from chosen location",
        "Location",
    ],
)

# Famous Tourist attractions in Amsterdam
dict_places = {'Vondelpark': (52.3579946, 4.8686484, 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=AfLeUgNhAMMrTZmO51l0oimmFFcXncWY9Vv4nwZt2Ee0mlmbm7uozsyMXlF1EvhdUz2AmUyO3Qtbj6WHfes_vJ_znjHB6puXlyeIsTsjUPjJKwvRz5gFvST_gl9Gb5Cz07KdNkaPALTELMl0k5MHP-WTOSQw1HUVvPN5EOWs0L8kg6Tqvz1I&key=AIzaSyC1UsciArxAvqmxs64NaR1ANVGjLztBECU'), 'Rijksmuseum': (52.3599976, 4.8852188, 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=AfLeUgNyVxZzQdRI1n1oiXlEv25rda016RxgSBTe12pBgLazXeSXNO8efvjXC8no6gHUrwuYjYZpn1OWL74cxturna2j5MKgojIKvaS4X-JxdPybiQL0eeHIBPsOAzc0naNOGDPsH-jKnluQwI70Gl62IV95EfMrwJV3ft3A4ln64YH691xW&key=AIzaSyC1UsciArxAvqmxs64NaR1ANVGjLztBECU'), 'Royal Palace Amsterdam': (52.3728073, 4.8913573, 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=AfLeUgNg_U0QR1fobLzuGc4IKk4EvnlfMa1UfsA8kY1rmCn4Hhnnpg4J2IJ6eswYvnUt9DpSvk5slCdkUf_2mATZU1I1KzgIBfqJ3BBux1NNvPOm8WfLXr_SDwRsqLFMSTAVAJ1sqEQYAzLFn3Qys94Hk5WCJm1C3L6mMFigguaXD__PRc3z&key=AIzaSyC1UsciArxAvqmxs64NaR1ANVGjLztBECU'), 'ARTIS': (52.3660003, 4.9165321, 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=AfLeUgMNnhmvBhUtzqU7E9rNsrPys-KItYGhYOWWuO_QEXBFyBCoUVkzDB7EEyHWz8dB7n5ERlHFipIeimdie3RPN_R9fnDW_T37IVZ7E59W8FnqFIqgtJ7Z9fgv6ddo-2GMCTKLYw_0GB97BDSZUFIVBFb8WKIIb9l73UVEr2z09VDW6w57&key=AIzaSyC1UsciArxAvqmxs64NaR1ANVGjLztBECU'), 'Munttoren': (52.367041, 4.8932901, 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=AfLeUgOYrhU5BroH0ZI1KSScpg3cJgnItLg-AzrfuCVutXntpfbd1y25aGN3SziiFatAPXSTgTNfvOtCU1uThsqtZ_3PkGHDeO_ahaoFNBySl0PmC4bkFcIub7ejBoVjm-UYGLYQPQx8nu-7eF-MvA0WkUn9e9jM0QRR15GCEeZZqd_mZKLC&key=AIzaSyC1UsciArxAvqmxs64NaR1ANVGjLztBECU'), 'Hortus Botanicus Amsterdam': (52.3666659, 4.9081845, 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=AfLeUgO71WeU8bvsNFmqXUc_CRt1fCCI17bk5sqQ5k7TFInBEs_RSGu3st2zGoq70zbkxSeRVig9wtE6gAb6HHd1g5m6e5q4qxXUDCxQ5GTuraIHF5YihkTOWpasOi5g8cVrualjenXN133flujWcy4eFf2VsvtECEdI5EyzevAO0rI51dy3&key=AIzaSyC1UsciArxAvqmxs64NaR1ANVGjLztBECU'), 'Dungeon Amsterdam': (52.3701599, 4.8921108, 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=AfLeUgOXaxqTPYuq9daYt_7kh_tv8BDY8z4IL1IOllQfPrZyNhYkKwWE3bx81JKr4YocHxXbq9f2FcQX27tGpQj-43qlwrVMscmZx5dNblNTJwynvM3vQgphYIEQNikhdLngQCNjla7M4gmHm-gTW078nvQghXxRqAjzctJJxYXEtugu5p0v&key=AIzaSyC1UsciArxAvqmxs64NaR1ANVGjLztBECU'), 'National Monument': (52.372681, 4.893618, 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=AfLeUgPCsYfIGmVlPsRDmRavT0YXJbT0c2PyjfQvAk3cMXLskZtvsl6PNnNPqsHdhJOZeD7bxucup_1b8ghctx_77XQJJUAZGfV89wS7XvLjFQh5cjbjHNOyFR0SA6F8eQhZY58o8YLIx2Q2PWbfm3r_KJ4qebYpZyEbewqeNeDxJqdl4AaO&key=AIzaSyC1UsciArxAvqmxs64NaR1ANVGjLztBECU'), 'NEMO Science Museum': (52.3737465, 4.912318099999999, 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=AfLeUgOcXWabNOWvGyYVSAtIJIgmI3emkUUCm-khTBgTf7Ig5jpYeHFyTgYTetYuwXtCinutc65CEiRVMmxCOV9uQRsTsX2DIVndNbYtXy3lJJzunVJ4KtV1Id7u8gItZBhWkfJEPyUGrIHdayyq5V87khXBf9lPEjBv70sZ418oO4uxceDj&key=AIzaSyC1UsciArxAvqmxs64NaR1ANVGjLztBECU'), 'Van Gogh Museum': (52.3584159, 4.8810756, 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=AfLeUgOzU3ySYDcodlTvbJIBhKg-4RD2JAh71Hmf0IHuv6YkVNu0bfl8JVrebtlIEeLg57tXNGsDXGSGwcV2jbmlU5RNhyVxdZkkBrCq8vc78inTmjAFZNmHmp_kslApH3Gw7NTbuszXOz76GTWRc-fdlm6cRlxLSDUvluvbwOGe5E37UMNU&key=AIzaSyC1UsciArxAvqmxs64NaR1ANVGjLztBECU'), 'Rembrandt Monument': (52.366004, 4.896562299999999, 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=AfLeUgPHolSmGu4rv5q0G26xL0KTutijcMtINKa4vrQLF3Iom0yQR2XU-vveZoHiS3KrjKue-yM968LSsY0cHRjQf1BI7_QtSssSoudFcR86FYymvf4nQd9RaAfYy-MSuZQojSf7UBchm4WvFNVSDQOOiZ3at6Epj4gGs7jFpkzy1KQr7qh_&key=AIzaSyC1UsciArxAvqmxs64NaR1ANVGjLztBECU'), 'WONDR Experience': (52.3854933, 4.9196798, 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=AfLeUgPzhUXOuWXlpFBZ0Y-61AmWhErZRdzS3Pd_PtnlGfaLtUT91rkLag2yStdmQ9S7YNI234wI2limh-jjgXJza1oT663GdCqJprVEleittX7abKa58JGQ_tQJcBVDAAZHdhjDfq2bb3EmPstJ-OBwoTxjpyZypJrIAmWV3lk7iPBQ8T9Y&key=AIzaSyC1UsciArxAvqmxs64NaR1ANVGjLztBECU'), 'Stedelijk Museum Amsterdam': (52.3580111, 4.879755400000001, 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=AfLeUgOG-Ys10nvcgSQ0lwh3BLNKaK___bUX1wXyeYpRax8P0zrRrRy02ITkaENi1TGb7yajWfrrrQyElA5BUwCLUVC3zyB5vUzvCfk7-Pmm7Tb47JE2usfNfahNrdJV5IwaKF9RSOe0XbLJmiaSnMMenx0QgqqylIkbnQ4GitjihudijMIm&key=AIzaSyC1UsciArxAvqmxs64NaR1ANVGjLztBECU'), 'Rembrandts Amsterdam Experience': (52.3623981, 4.883524200000001, 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=AfLeUgPxpIzt90fHzrJ067vBHlVzJuFGpbWQBuZZzjZXLRvjZ7eZ8S7L3_-NAYesuTrkpR6j37y7RMESnc_-2chQ60nYmdqjIgbRwjxR4XdcetGNtc0tEMg4FSxJTz5KBF3mT24O79PE-Fh7LYZS_EM_ZPBDPh8qJ7TD6wW28yzRzzITHoB0&key=AIzaSyC1UsciArxAvqmxs64NaR1ANVGjLztBECU'), 'Anne Frank House': (52.3752103, 4.8839503, 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=AfLeUgMIB3hG6oaUrh9zMQLq-8rqyK4il9tbyQY-rXrxJSVmOlROo64zjV49o1OmT4QnRpv7HMUMUPbuo8GyjeqrqsEaH7BH1BMFp6MkwMKSgR0wWWR_Ak_RZJfrQ_U30cbLnDmHCY11p1z98qD5CQWzGq-YRcGyxu1KITKBJFpjIFkAi0mN&key=AIzaSyC1UsciArxAvqmxs64NaR1ANVGjLztBECU'), 'Westerkerk': (52.3745941, 4.883975299999999, 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=AfLeUgMhPsYRBRecdX-Jz9HFmsxZcQ77wTo8T2Gg9Ztu5w8E_2vzP2HZT2T553xRhLKsicNZG9Zj8iqTSr5DyW8YTxZA4XuuQwImQ6lKM5PPuEOVOwRLQUdVdb9hpGXEmlwi02ByVLNe3ibMoKIVhYqsIo-JeJfmylV925P2cp64hnNCAudZ&key=AIzaSyC1UsciArxAvqmxs64NaR1ANVGjLztBECU'), 'The National Maritime Museum': (52.3716667, 4.915, 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=AfLeUgOhV2_Sc1Ug7IRTrw3ANBuU5SgJyQK5jNiwNA3bVa60jSTmKfO0xaFN7qVnpx79V9zVayoIg_peWOp_PCYRA-zeVChT7XBq_H1v45FFF_J1QPJqlWr7t7wV1cLpE8QtkqRwS_69Zqj8S-Ya1KxkHShW5Md6rX3UtP_kSBDKtl2MxMc&key=AIzaSyC1UsciArxAvqmxs64NaR1ANVGjLztBECU'), 'Eye Film Museum': (52.384348, 4.901276, 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=AfLeUgMCiA-8p2x_7zpPxLea99TeEl_ND1rekz58WdUrw6bH6PrmDzhr5UERxXf2p8VKbVSiRYcik0Ttk4vhzSZcbBLmXCLWUOmYo9KLwy4KUszIJWWEOzK-3ItHixPwaKZ8nCmean5_8wFCSfSIoUVNCHm0KIpFNCCn1gudR5h7YCUfrN9N&key=AIzaSyC1UsciArxAvqmxs64NaR1ANVGjLztBECU'), 'Hermitage Amsterdam': (52.3652692, 4.902419000000001, 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=AfLeUgNKKS6a8o_BLzCD1PWH8pUqk1nmYE501LuWYHWfMhYkVvZ4xDn-c2Zn7qzFe32hr8GbWtQhmf6nqOZTrK2TBMP0YTrGsJZogJxG8AU3oRaN7-tNY_PnixNrCi0Pl9odLcqV-NjlnWVF3pXNMMpBebjGH91BmhuXYvWOIGsUjxOzyQ3E&key=AIzaSyC1UsciArxAvqmxs64NaR1ANVGjLztBECU'), "Ripley's Believe It or Not!": (52.3724001, 4.8935666, 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=AfLeUgOcTHocJCDMeOzZgcjqcuD6JjjETggKNdKk2Ntz9GSL7z37DkI_ddxm9YV9lBjfv3CPwtFAo0jw49TOBO3oJ_YvZ-oUaswn4QF3MpRvEcbMhacUMKVLAYdyKGx_lFmYRwgz4VtdTfaa858CBN39_qwpwqXBCbShwT7H9naOtAZCYtfa&key=AIzaSyC1UsciArxAvqmxs64NaR1ANVGjLztBECU')}
list_places = dict_places.keys()
# Chose a place and show image
chosen_place = st.sidebar.selectbox('Select a Location: ',(list_places),index=17)
st.sidebar.image(dict_places[chosen_place][2], caption=None, width=None,
                 use_column_width=None, clamp=False, channels="RGB",output_format="auto")

# Change chosen location on the dataframe
dataframe.at[0, 'Latitude'] = dict_places[chosen_place][0]
dataframe.at[0, 'Longitude'] = dict_places[chosen_place][1]
dataframe['Location'] = 0
dataframe.at[0, 'Location'] = 1

def from_location_to_airbnb_listing_in_meters(lat1: float, lon1: float, lat2: list, lon2: list):   
    R = 6371000  # Radius of Earth in meters
    phi_1 = np.radians(lat1)
    phi_2 = np.radians(lat2)
    delta_phi = np.radians(lat2 - lat1)
    delta_lambda = np.radians(lon2 - lon1)
    a = (
        np.sin(delta_phi / 2.0) ** 2
        + np.cos(phi_1) * np.cos(phi_2) * np.sin(delta_lambda / 2.0) ** 2
    )
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    meters = R * c  # Output distance in meters
    return np.round(meters, 0)


dataframe['Meters from chosen location'] = dataframe.apply(
    lambda row: from_location_to_airbnb_listing_in_meters(row['Latitude'],row['Longitude'],dict_places[chosen_place][0],dict_places[chosen_place][1]),axis=1
    )

# We have a limited budget, therefore we would like to exclude
# listings with a price above 10000 rupees per night
dataframe = dataframe[dataframe["Price"] <= 10000]

# Display as integer
dataframe["Airbnb Listing ID"] = dataframe["Airbnb Listing ID"].astype(int)
# Round of values
dataframe["Price"] = "₹ " + dataframe["Price"].round(2).astype(str) # <--- CHANGE THIS POUND SYMBOL IF YOU CHOSE CURRENCY OTHER THAN POUND - Changed to INR symbol
# Rename the number to a string
dataframe["Location"] = dataframe["Location"].replace(
    {1.0: "To visit", 0.0: "Airbnb listing"}
)

# Display dataframe and text
st.dataframe(dataframe)
st.markdown("Below is a map showing all the Airbnb listings with a red dot and the location we've chosen with a blue dot.")

# Create the plotly express figure
fig = px.scatter_mapbox(
    dataframe,
    lat="Latitude",
    lon="Longitude",
    color="Location",
    color_discrete_sequence=["blue", "red"],
    zoom=11,
    height=500,
    width=800,
    hover_name="Price",
    hover_data=["Meters from chosen location", "Location"],
    labels={"color": "Locations"},
)
fig.update_geos(center=dict(lat=dataframe.iloc[0][2], lon=dataframe.iloc[0][3]))
fig.update_layout(mapbox_style="stamen-terrain")

# Show the figure
st.plotly_chart(fig, use_container_width=True)
