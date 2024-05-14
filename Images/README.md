Here is your formatted and professional documentation for the images directory, ready for copying and pasting:

---

# Images Directory

This directory is divided into three different folders: Flow_Diagrams, Schemas, and UI_Sketches. Their content is explained below:

## Flow_Diagrams

This folder displays flow diagrams, showing information flux and necessities.

### Flow_Diagram 1 - Item Update on Inventory

The volunteer takes information about the neighbor's usage of inventory items and updates the inventory accordingly.

![Flow Diagram 1]( Images/Flow_Diagrams/Flow_Diagram_1.png)

### Flow_Diagram 2 - Creating and Changing Neighbor Information on Database

The Neighbor provides information on themselves, which the volunteer uses to update their profile.

![Flow Diagram 2]( Images/Flow_Diagrams/Flow_Diagram_2.png)

### Flow_Diagram 3 - Assisting a Neighbor and Recording Services Use

The Neighbor is offered services available, and requests volunteer assistance. The volunteer connects the neighbor with the partners needed for their necessity.

![Flow Diagram 3]( Images/Flow_Diagrams/Flow_Diagram_3.png)

### Flow_Diagram 4 - Flow of Information for Service Recording

The regular interaction between neighbor and volunteer. The neighbor can either use a service or register their information with UP. If information is registered regarding the neighbor, the neighbor table is updated. If the neighbor uses a service, the visit_service table is updated.

![Flow Diagram 4]( Images/Flow_Diagrams/Flow_Diagram_4.png)

## Schemas

This folder contains the conceptual and relational schemas throughout the project.

### Conceptual Schemas

The chronological order of schemas will be displayed, with an explanation of why they needed updates.

#### Initial Schema

Created in mid-February, there were 6 entities, and they were not enough to explain the complexity of work conducted by UP. The original idea of keeping the entity "records" as the central piece of information was kept.

![Initial Schema](Images/Schemas/Conceptual_Schema_02_15_24.png)

#### Second Schema

The schema as a whole was rethought. Ensuring coherence was a priority, therefore, "partner organizations" were reestablished into "service_provider" to dialogue with the original description of services. "Services" was broken down into two parts: "Service", which describes the kind of service an organization provides, and "Visit Service", which is a log of what kind of service was provided to the neighbor. The entity "Case Managers" was renamed "Volunteer", to reflect that "case management" is the official title for a service provided by one of UP's partners.

![Second Schema]( Images/Schemas/Conceptual_Schema_02-28-24.png)

#### Third Schema

The entity "Service_Provider" was updated to allow UP to also provide a service (since besides their main work as a centralized resource reference for neighbors, they provide their own service as well). UP's main goal is to keep information easily accessible, therefore they need specific information on what products are entering and leaving their inventory. Thus, the table "Inventory_Usage" was created, and it centralized which items have been used and updates it in the inventory.

![Third Schema]( Images/Schemas/Conceptual_Schema_03-26-24.png)

#### Final Schema

The final conceptual schema includes minor changes to ensure usability. Firstly, each entity has an internal ID number. Additionally, "Inventory" and "Inventory_Usage" had their attributes and primary keys updated to ensure usability.

![Final Schema]( Images/Schemas/Conceptual_Schema_04-03-2024.png)

### Relational Schemas

These two relational schemas demonstrate how the database interconnects through its tables and foreign keys. They use the conceptual schemas of 02/13/24, and 02/28/24.

First Relational Schema:

![First Relational Schema]( Images/Schemas/Relational_Schema_02_15_24.png)

Second Relational Schema:

![Second Relational Schema]( Images/Schemas/Relational_Schema_02_28_24.png)

### Normalization Schemas

There are two files showing normalization parameters. They analyze the conceptual schemas from 03/18/24 and 03/27/24. Each of them demonstrates normalization on the third form, which is correct and updated in the second version.

First Normalization:

![First Normalization]( Images/Schemas/Normalization_Schema_03-20-24.jpg)

Second Normalization:

![Second Normalization]( Images/Schemas/Normalization_Schema_03-27-24.png)

## UI Sketches
-> There are two UI Sketches in this folder. They consist of initial plans for the application visual. The final result of those sketches follows the initial plan, with menus and main options in the left side bar, and information displayed in the center. Below are the original sketches:

1 - Website conceptual visuals, with information displayed in the center and referenced in the left.
![brief alt text]( Images/UI_Sketches/UI_1.png)

2 - Pages reference
![brief alt text]( Images/UI_Sketches/UI_2.png)