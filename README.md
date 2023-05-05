# Indian Banks API

This Django project provides REST API endpoints to retrieve details of banks and their branches in India. The data is sourced from the CSV file bank_branches.csv stored in a GitHub [repository](https://github.com/Amanskywalker/indian_banks).

## _Quickview_
To have a quick view of all the endpoints of the API server, head to this [link](https://web-production-fe52.up.railway.app/).

## Endpoints
- /banks - outputs JSON response of all banks with their names and bank ids.
- /branches/<bank_id> - outputs JSON response of all branches with the given bank_id
- /ifsc/<ifsc_code>/ - outputs JSON response all the branch having the given ifsc_code
- By default the home page of the server displays the '/banks' endpoint.


## Implementation
- The API server is developed using django-restframework.
- We have used the requests module to get response from the site where the csv file is stored.
- This response is converted to a dictionary and returned as a list.
- Then we implement three functions in the views.py file to retrieve data.
    - bank_list - this function returns all the banks with their names and bank ids.
    - branch_list - this function takes a parameter bank_id and returns all the respective branches.
    - ifsc_details - this function takes a parameter ifsc_code and returns the respective branch details.
- We have migrated all the migrations after defining the data format in models.py
- urls.py of the app is configured with the project's urls.py
- For deployment, we have used the railway.app service.
- The app is hosted on the URL - https://web-production-f268.up.railway.app/
- All the endpoints can be tested on this URL.
