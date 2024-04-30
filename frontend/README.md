## 2 -> Frontend
Contains information for the frontend portion of UP application. It is divided in two sub-folders: public (a system convention, for this application it contains UP logo file used in the web application) and src (containing the code for the application's frontend). The other files in the folder (babel.config.js, jsconfig.json, package-lock.json, package.json, vue.config.js) are system files to ensure the operationality of json, javascript, and vue, main parts of the application. src, the file with the coding portion uses the framework vue for frontend development, and it is explained below:

### src 
# Frontend Folder Structure
### Folders
This folder contains the source code for the frontend application. It includes the following subfolders:

components: This folder contains reusable UI components that are used throughout the application.
pages: This folder contains the different pages of the application, each representing a specific route or view.
assets: This folder contains static assets such as images, fonts, or other media files used in the application.
router: This folder contain the file index.js, which defines the routes for the application. It maps URLs to specific components or pages.
views: This folder contains .vue framework usage. To ensure usability and UI advances, UP application uses .vue, which compiles the information and makes the backend-frontend correspondence.
