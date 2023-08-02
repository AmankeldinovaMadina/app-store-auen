import streamlit as st


def policy_page():
    st.title("Auen-AI Privacy Policy")
    st.write("Effective Date: 02.08.2023")

    st.subheader("Privacy Policy")
    st.write(
        "Auen-AI built the BookIt AI app as a Free app. This SERVICE is provided by BookIt AI at no cost and is intended for use as is. This page is used to inform visitors regarding our policies with the collection, use, and disclosure of Personal Information if anyone decided to use our Service. If you choose to use our Service, then you agree to the collection and use of information in relation to this policy. The Personal Information that we collect is used for providing and improving the Service. We will not use or share your information with anyone except as described in this Privacy Policy. The terms used in this Privacy Policy have the same meanings as in our Terms and Conditions, which are accessible at BookIt AI unless otherwise defined in this Privacy Policy."
    )

    st.subheader("Information Collection and Use")
    st.write(
        "Microphone Usage: Our App requires access to your device's microphone to record your voice for converting it into music sheets and piano sounds. We do not collect or store any audio recordings of your voice. Instead, the recorded voices are used solely for the purpose of real-time conversion into piano sounds."
        "\n\n"
        "Converted Piano Sounds: The piano sounds generated from your voice may be saved temporarily within the App to ensure proper functionality during your current session. However, we do not permanently store or retain any converted piano sounds on our servers or in any identifiable form."
    )

    st.subheader("Log Data")
    st.write(
        "We want to inform you that whenever you use our Service, in a case of an error in the app we collect data and information (through third-party products) on your phone called Log Data. This Log Data may include information such as your device Internet Protocol (“IP”) address, device name, operating system version, the configuration of the app when utilizing our Service, the time and date of your use of the Service, and other statistics."
    )

    st.subheader("Cookies")
    st.write(
        "Cookies are files with a small amount of data that are commonly used as anonymous unique identifiers. These are sent to your browser from the websites that you visit and are stored on your device's internal memory. This Service does not use these “cookies” explicitly. However, the app may use third-party code and libraries that use “cookies” to collect information and improve their services. You have the option to either accept or refuse these cookies and know when a cookie is being sent to your device. If you choose to refuse our cookies, you may not be able to use some portions of this Service."
    )

    st.subheader("Service Providers")
    st.write(
        """
        We may employ third-party companies and individuals due to the following reasons:

            - To facilitate our Service;
            - To provide the Service on our behalf;
            - To perform Service-related services; or
            - To assist us in analyzing how our Service is used.
            
        We want to inform users of this Service that these third parties have access to their Personal Information. The reason is to perform the tasks assigned to them on our behalf. However, they are obligated not to disclose or use the information for any other purpose.
        """
    )

    st.subheader("Security")
    st.write(
        "We value your trust in providing us your Personal Information, thus we are striving to use commercially acceptable means of protecting it. But remember that no method of transmission over the internet, or method of electronic storage is 100% secure and reliable, and we cannot guarantee its absolute security."
    )

    st.subheader("Links to Other Sites")
    st.write(
        "This Service may contain links to other sites. If you click on a third-party link, you will be directed to that site. Note that these external sites are not operated by us. Therefore, we strongly advise you to review the Privacy Policy of these websites. We have no control over and assume no responsibility for the content, privacy policies, or practices of any third-party sites or services."
    )

    st.subheader("Children’s Privacy")
    st.write(
        "We do not knowingly collect personally identifiable information from children. We encourage all children to never submit any personally identifiable information through the Application and/or Services. We encourage parents and legal guardians to monitor their children's Internet usage and to help enforce this Policy by instructing their children never to provide personally identifiable information through the Application and/or Services without their permission. If you have reason to believe that a child has provided personally identifiable information to us through the Application and/or Services, please contact us. You must also be at least 16 years of age to consent to the processing of your personally identifiable information in your country (in some countries we may allow your parent or guardian to do so on your behalf)."
    )

    st.subheader("Changes to This Privacy Policy")
    st.write(
        "We may update our Privacy Policy from time to time. Thus, you are advised to review this page periodically for any changes. We will notify you of any changes by posting the new Privacy Policy on this page."
    )
    st.write("This policy is effective as of 2023-08-02")

    st.subheader("Contact Us")
    st.write(
        "If you have any questions or suggestions about our Privacy Policy, do not hesitate to contact us at  madina.amankeldinova@nu.edu.kz."
    )


def support_page():
    st.title("Auen-AI App Support")
    st.write(
        "Welcome to our App Support Page. Should you have any queries, require assistance with specific features, or even if you just wish to engage with us, please feel free to contact us at madina.amankeldinova@nu.edu.kz."
    )

def main():
    st.title("Auen-AI App Store")
    pages = ["Privacy Policy", "App Support"]
    selected_page = st.selectbox("Navigation", pages)

    if selected_page == "Privacy Policy":
        policy_page()
    elif selected_page == "App Support":
        support_page()


if __name__ == "__main__":
    main()




