<!-- 🔥 HERO BANNER -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:11998e,100:38ef7d&height=200&section=header&text=Churn Predictor &fontSize=40&fontColor=ffffff&animation=fadeIn" />
</p>

<h1 align="center">📊 Churn Predictor</h1>
<h3 align="center">AI-Powered Customer Churn Prediction System</h3>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Model-Random%20Forest-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Production--Ready-success?style=for-the-badge" />
</p>

<hr/>

<h2>🧠 Overview</h2>
<p>
<b>Churn Predictor</b> is a machine learning-based system designed to predict whether a customer will churn (leave) or stay with a company. 
It helps businesses identify high-risk customers early and take preventive actions.
</p>

<p>
<b>Goal:</b> Reduce customer loss using intelligent prediction models.
</p>

<blockquote>
💡 Use Case: Telecom • Banking • SaaS • Subscription Platforms
</blockquote>

<hr/>

<h2>⚙️ ML Pipeline</h2>

<pre>
Data Loading → EDA → Preprocessing → Encoding → 
Train/Test Split → Model Training → Evaluation → Hyperparameter Tuning
</pre>

<hr/>

<h2>✨ Key Features</h2>

<table>
<tr><th>Feature</th><th>Description</th></tr>
<tr><td>🔍 Multi-Model Training</td><td>Logistic Regression, Random Forest, SVM, XGBoost</td></tr>
<tr><td>📊 EDA</td><td>Data analysis and visualization</td></tr>
<tr><td>⚡ High Accuracy</td><td>~90% with tuned Random Forest</td></tr>
<tr><td>🔧 Hyperparameter Tuning</td><td>GridSearchCV optimization</td></tr>
<tr><td>📈 Evaluation Metrics</td><td>Accuracy, Confusion Matrix, Classification Report</td></tr>
<tr><td>🧠 Smart Prediction</td><td>Identify churn risk customers</td></tr>
</table>

<hr/>

<h2>🤖 Models Used</h2>

<table>
<tr><th>Model</th><th>Type</th><th>Performance</th></tr>
<tr><td>Logistic Regression</td><td>Linear</td><td>Baseline</td></tr>
<tr><td>Random Forest</td><td>Ensemble</td><td>⭐ Best (~90%)</td></tr>
<tr><td>SVM</td><td>Classification</td><td>Strong</td></tr>
<tr><td>XGBoost</td><td>Boosting</td><td>High accuracy</td></tr>
<tr><td>Decision Tree</td><td>Tree-based</td><td>Moderate</td></tr>
</table>

<hr/>

<h2>📊 Performance Insights</h2>

<ul>
  <li>✅ Random Forest achieved highest accuracy (~0.90)</li>
  <li>📉 Balanced precision and recall</li>
  <li>📊 Confusion matrix used for evaluation</li>
  <li>🔁 5-Fold Cross Validation applied</li>
</ul>

<hr/>

<h2>📂 Dataset</h2>

<p><b>Bank Customer Churn Dataset (~10,000 records)</b></p>

<table>
<tr><th>Feature</th><th>Description</th></tr>
<tr><td>CreditScore</td><td>Customer credit score</td></tr>
<tr><td>Geography</td><td>Customer country</td></tr>
<tr><td>Gender</td><td>Male/Female</td></tr>
<tr><td>Age</td><td>Customer age</td></tr>
<tr><td>Tenure</td><td>Years with bank</td></tr>
<tr><td>Balance</td><td>Account balance</td></tr>
<tr><td>NumOfProducts</td><td>Products used</td></tr>
<tr><td>HasCrCard</td><td>Credit card status</td></tr>
<tr><td>IsActiveMember</td><td>Active membership</td></tr>
<tr><td>EstimatedSalary</td><td>Salary</td></tr>
</table>

<p><b>Target:</b> Exited (1 = Churn, 0 = Stay)</p>

<hr/>

<h2>🛠️ Tech Stack</h2>

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,numpy,pandas,sklearn,matplotlib,seaborn" />
</p>

<ul>
  <li>NumPy & Pandas → Data processing</li>
  <li>Matplotlib & Seaborn → Visualization</li>
  <li>Scikit-learn → Machine Learning models</li>
</ul>

<hr/>

<h2>📁 Project Structure</h2>

<pre>
ChurnSenseAI/
├── churn.ipynb
├── Churn_Modelling.csv
├── README.md
</pre>

<hr/>

<h2>💻 Usage</h2>

<pre>
# Train model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, y_pred))
</pre>

<hr/>

<h2>📊 Engineering Highlights</h2>

<ul>
  <li>⚡ Multi-model comparison</li>
  <li>🧠 Strong generalization</li>
  <li>📈 Hyperparameter tuning (GridSearchCV)</li>
  <li>📊 Clear evaluation metrics</li>
</ul>

<hr/>

<h2>🔮 Future Enhancements</h2>

<table>
<tr><th>Feature</th><th>Description</th></tr>
<tr><td>🌐 Streamlit App</td><td>Interactive web UI</td></tr>
<tr><td>📊 Dashboard</td><td>Visualization with Plotly</td></tr>
<tr><td>🤖 Deep Learning</td><td>ANN-based prediction</td></tr>
<tr><td>📡 API</td><td>FastAPI deployment</td></tr>
</table>

<hr/>

<h2>👩‍💻 Author</h2>

<p align="center">
  <b>Anushka Singh</b><br/>
  AI Engineer | Machine Learning | Data Science
</p>

<hr/>

<h2 align="center">⚡ Final Insight</h2>

<p align="center">
<b>"Predicting churn is not just about data — it's about understanding customer behaviour."</b>
</p>

<hr/>

<p align="center">
⭐ Star this repository if you found it useful!
</p>
