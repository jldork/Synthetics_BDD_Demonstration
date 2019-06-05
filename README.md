# Synthetic User Journey Testing written in BDD style

### Setup Instructions
Check your chrome browser version
![check](https://user-images.githubusercontent.com/1771806/58942453-b474fd00-8775-11e9-9d01-5e3fb4f1cc94.png)

Then download the chrome driver from http://chromedriver.chromium.org/downloads and extract the binary into your $PATH

```
# Clone this repo
# Set up virtual environment
virtualenv venv -p python3
source venv/bin/activate

# Install Behave and Selenium
pip install -r requirements.txt
```

To run the tests, simply type the command `behave`
