import streamlit as st

from main import ann_app

def main():
    st.title('Heart Disease Prediction using Artificial Neural Networks (ANN)')
    menu=['Home','Model','Metrics','About']
    choice=st.sidebar.selectbox('Menu',menu)
    if choice=='Home':
        st.subheader('Introduction')
        st.write('')
        
        st.write("""Heart disease prediction using Artificial Neural Networks (ANN) is a popular approach in the field of medical research and diagnosis. ANN is a machine learning technique that can learn patterns and relationships within data to make predictions or classifications. In the context of heart disease prediction, an ANN can analyze various features or attributes related to a patient's health and provide insights into the likelihood of developing heart disease.

The dataset you provided consists of several columns or features that can be used for heart disease prediction. Let's discuss each of these features:

1. AGE: This column represents the age of the patient. Age is an essential factor in determining the risk of heart disease, as the incidence of heart-related issues generally increases with age.

2. GENDER: This column indicates the gender of the patient. Gender can play a role in assessing the risk of heart disease, as certain conditions may be more prevalent in males or females.

3. CHEST_PAIN: This column describes the type of chest pain experienced by the patient. Different types of chest pain can be indicative of various heart conditions, and their presence can help in diagnosing potential heart disease.

4. RESTING_BP: This column represents the resting blood pressure of the patient. Elevated blood pressure is a significant risk factor for heart disease.

5. SERUM_CHOLESTEROL: This column denotes the serum cholesterol levels of the patient. High levels of cholesterol in the blood can contribute to the development of heart disease.

6. TRI_GLYCERIDE: This column represents the triglyceride levels in the patient's blood. Elevated triglyceride levels are associated with an increased risk of heart disease.

7. LDL: This column indicates the low-density lipoprotein (LDL) cholesterol levels. High levels of LDL cholesterol can contribute to the formation of plaque in the arteries, leading to heart disease.

8. HDL: This column represents the high-density lipoprotein (HDL) cholesterol levels. HDL cholesterol is often referred to as "good" cholesterol, as it helps remove LDL cholesterol from the bloodstream and can lower the risk of heart disease.

9. FBS: This column denotes the fasting blood sugar levels of the patient. Elevated fasting blood sugar levels can indicate the presence of diabetes, which is a risk factor for heart disease.

10. RESTING_ECG: This column describes the results of the resting electrocardiogram (ECG) test. The ECG can provide information about the electrical activity of the heart and help diagnose certain heart conditions.

11. MAX_HEART_RATE: This column represents the maximum heart rate achieved during exercise. Abnormal heart rate responses can indicate underlying heart problems.

12. ECHO: This column indicates the results of an echocardiogram, which is an ultrasound test that provides images of the heart's structure and function. Echocardiograms can assist in diagnosing various heart diseases.

13. TMT: This column represents the results of the Treadmill Test (also known as the Exercise Stress Test), which measures the heart's response to exercise. Abnormalities during the test can indicate potential heart disease.

By utilizing an ANN model, you can train the network using this dataset, with the columns mentioned above as input features, and a target variable indicating the presence or absence of heart disease. The ANN will learn the patterns and relationships between these features and the corresponding outcomes, allowing it to make predictions about heart disease for new, unseen data.

It is important to note that the accuracy and reliability of the predictions generated by the ANN model will depend on the quality and representativeness of the dataset, as well as the appropriate preprocessing and feature engineering techniques applied. Additionally, the model should be validated using appropriate evaluation metrics and cross-validation techniques to ensure its generalizability.""")
        
        st.write('')
        
    elif choice=='Model':
        ann_app()
        
    elif choice=="Metrics":
        with open('exp.html', 'r',  encoding='utf-8') as f:
            html_content = f.read()
        st.components.v1.html(html_content, height=800)
        f.close()
   
    else:
        st.subheader('About')
 
        st.write("""Selecting a project related to heart disease prediction using ANN can be a valuable and impactful choice. Here are some reasons why this project can be a good selection:

1. Significance of the problem: Heart disease is a leading cause of mortality worldwide, and early detection plays a crucial role in improving patient outcomes. By developing a heart disease prediction model, you can contribute to the field of healthcare by providing a tool that helps identify individuals at risk and facilitates early intervention.

2. Availability of relevant data: The dataset you mentioned contains several important features associated with heart disease, such as age, sex, chest pain type, blood pressure, cholesterol level, and more. Having a well-curated dataset is essential for training an accurate and reliable ANN model. With the availability of this dataset, you have a solid foundation to start your project.

3. Technological advancements: Artificial Neural Networks have proven to be effective in various applications, including medical diagnostics. ANN models have the ability to capture complex relationships and patterns in the data, making them suitable for predicting heart disease risk based on multiple input variables.

4. Interdisciplinary nature: This project combines elements from both healthcare and machine learning fields. By working on such a project, you have the opportunity to enhance your skills in data preprocessing, model development, and evaluation techniques, as well as gain insights into cardiovascular health.

5. Potential for real-world impact: The ultimate goal of this project is to create a predictive model that can assist healthcare professionals in making informed decisions. The implementation of a heart disease prediction system can help identify high-risk individuals, enabling timely interventions, lifestyle modifications, and appropriate medical treatments. By contributing to this area, you can have a positive impact on public health.

6. Learning opportunities: Undertaking a project on heart disease prediction using ANN allows you to delve into the principles and techniques of machine learning, neural networks, and data analysis. You can gain hands-on experience in data preprocessing, model training, hyperparameter tuning, and performance evaluation, which are valuable skills in the field of artificial intelligence and data science.

Overall, selecting a project focused on heart disease prediction using ANN offers a meaningful and challenging opportunity to leverage machine learning techniques for healthcare purposes. By addressing a critical health issue and developing a predictive model, you can make a difference in patient care and contribute to advancements in medical research.""")
        
        st.subheader('Future Scope')
        
        st.write(""" The future scope for a heart disease prediction project using ANN is promising, as it opens up avenues for further research, advancements, and potential applications. Here are some potential future directions and scope for the project:

1. Refining the predictive model: As technology advances and more data becomes available, there is an opportunity to refine the heart disease prediction model. Researchers can explore different ANN architectures, activation functions, and optimization algorithms to improve the accuracy and efficiency of the model. Additionally, feature selection techniques and ensemble methods can be employed to enhance the predictive power of the model.

2. Integration with healthcare systems: The developed heart disease prediction model can be integrated into existing healthcare systems, such as electronic health records (EHR) or clinical decision support systems. This integration would enable healthcare professionals to utilize the model in real-time to assess the risk of heart disease for their patients, aiding in personalized treatment planning and preventive care.

3. Expansion to other risk factors and diseases: While the current project focuses on heart disease prediction using specific risk factors, future work can involve incorporating additional risk factors or expanding the scope to predict other cardiovascular diseases. Including factors like genetic predisposition, lifestyle habits, socioeconomic factors, and environmental factors can provide a more comprehensive understanding of disease risk and prevention.

4. Mobile applications and wearables: With the proliferation of mobile devices and wearables, there is an opportunity to develop mobile applications or wearable devices that leverage the heart disease prediction model. This would allow individuals to monitor their own health, receive personalized risk assessments, and receive early warnings for potential heart disease risks.

5. Incorporating advanced data sources: Future research can explore the integration of advanced data sources, such as genetic data, omics data (e.g., proteomics, metabolomics), and imaging data (e.g., echocardiograms, coronary angiograms). By incorporating these additional data types into the model, researchers can gain deeper insights into the underlying mechanisms of heart disease and improve the accuracy of predictions.

6. Clinical decision support and patient management: The heart disease prediction model can be further developed into a clinical decision support tool. It can assist healthcare professionals in making informed decisions regarding treatment plans, medication prescriptions, and lifestyle modifications. Moreover, the model can aid in patient management by identifying high-risk individuals who require closer monitoring and interventions.

7. Long-term outcome predictions: Extending the project to predict long-term outcomes, such as the risk of heart failure, stroke, or mortality, can provide valuable insights into disease progression and patient prognosis. This would require longitudinal data and continuous monitoring of patients over time.

It is important to note that the future scope of the project will largely depend on data availability, technological advancements, collaborations with healthcare institutions, and the evolving landscape of healthcare and machine learning. However, by addressing these potential directions, the project can contribute to the development of more accurate and personalized approaches for heart disease prevention, management, and patient care.""")        

        st.subheader("Created by : Fatima Zohra M.Tech (Biotechlogy), NIT Warangal")

main()

