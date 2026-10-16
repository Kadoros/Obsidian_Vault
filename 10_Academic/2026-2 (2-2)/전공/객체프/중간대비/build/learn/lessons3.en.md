@unit U3 | Object-Oriented Design (IIKH) | L03 Object-Oriented Design.pdf (Budd Ch.3)
@intro Responsibility-driven design and the 9-step development process, the IIKH example, characteristics of components (coupling/cohesion, interface/implementation), integration and stubs, maintenance. Coupling/cohesion blanks appeared in 2024·2023·2022·2019·2016, and essays on stubs and "slowly integrated" are regulars too.

@lesson L3-1 | Responsibility-Driven Design · Development Process · Scenarios | L03 p.2–9

## Responsibility Driven Design {#rdd}

- OOP = a set of interacting objects
- Each object is a component that has **responsibility** in a community
- The system is divided into the various activities it has to perform; those activities (responsibilities) are then **distributed** among the objects in the system
- After completing a list of responsibilities, decide on a set of objects and determine which responsibilities should be assigned to which object
- **Responsibilities in an object should be closely related**
- Design process: an imprecise, ambiguous, unclear **specification** → a **software system design** with concrete logic

## The 9-Step Development Process {#dev-process}

1. **Initial Description** (Specification)
2. **Refine Specification** (scenarios)
3. **Identification of Components**
4. **Identification of Components Responsibilities** (CRC cards)
5. **Formalize the Interface**
6. **Designing the Subsystem**
7. **Implementing Components** (+ unit test)
8. **Integration of Components** (stubs)
9. **Maintenance & Evolution**

## IIKH and Scenarios {#scenario}

- **IIKH (Intelligent Interactive Kitchen Helper)**: a PC-based application that replaces the box of recipe index cards in the kitchen. Maintains a recipe database + plans meals for an extended period (say a week), automatically scales recipes to any number of servings, prints menus for the week/day/meal, prints an integrated grocery list
- The initial description is **ambiguous and unclear** (the president drew it on the back of a dinner napkin) → the ambiguities must be clarified
- **Refining the specification = walking through scenarios**: **pretend** we already had a working application and walk through the various uses of the system
  - Establish the "look and feel", make sure we have uncovered all the intended uses, develop descriptive documentation, create the high-level software design
  - Other authors use the term **use-cases** (a set of scenarios of system usage)
- IIKH abilities: browse the recipe database, add a new recipe, edit or annotate a recipe, plan a meal of several courses, scale a recipe for some number of people, plan a longer period (a week), generate a grocery list

@lesson L3-2 | Identifying Components · CRC Cards · The Six IIKH Components | L03 p.10–18

## Component {#component}

- **An abstract design entity** with which we can associate responsibilities for different tasks
- Must have **a small well-defined set of responsibilities**
- Should interact with other components **to the minimal extent possible**

## CRC Cards {#crc}

- Components are most easily described using **CRC cards**: **C**omponent (name), **R**esponsibility (description of its responsibilities), **C**ollaborators (list of other components it works with)
- e.g. **Greeter**: responsibilities = display an informative welcome message, offer the user choices, pass control to the Recipe Database Manager or the Plan Manager / collaborators = Database Manager, Plan Manager

## The Six IIKH Components {#iikh-components}

| Component | Responsibilities |
|---|---|
| **Greeter** | welcome window at startup; lets the user browse the recipe database, add a new recipe, edit/annotate a recipe, review or create a meal plan |
| **Recipe Database** | maintains the recipe database, allows browsing, permits editing/annotating existing recipes, adding new recipes |
| **Recipe** | maintains the list of ingredients and the transformation algorithm, edits its own data, displays itself on the screen, prints itself |
| **Planner** (Plan Manager) | selects a sequence of dates for planning, edits an existing plan, associates with Date objects |
| **Date** | edits specific meals, annotates dates ("Bob's Birthday"), prints the grocery list for the entire set of meals |
| **Meal** | holds information about a single meal, interacts with the recipe database to select recipes, sets the number of people → recipes scaled automatically, grocery list for the meal |

- Everything can be accomplished with only six components → at this point the components can be **assigned to different programmers** for development

> Exam point: 2025 essay "In project 1 (IIKH), main difference between Recipe class and RecipeDB class?" → Recipe maintains the data of **a single** recipe and edits/displays/prints itself; RecipeDB manages the **collection** of recipes (browse, search, add, edit).

@lesson L3-3 | Characteristics of Components: Behavior/State, Coupling/Cohesion, Interface/Implementation | L03 p.19–25

## Behavior and State · Instances and Classes {#behavior-state}

- **Behavior**: the set of actions a component can perform
- **State**: all the information (data values) held within a component. It is common for behavior to change state
- **Instances and Classes**: there are many instances of Recipe, but they all behave the same way → we say the behavior is **common to the class Recipe**

## Coupling and Cohesion {#coupling-cohesion}

| | Definition | Goal |
|---|---|---|
| **Cohesion** | the degree to which the tasks assigned to a component seem to form **a meaningful unit** (how strongly its responsibilities are related) | **maximize** |
| **Coupling** | the degree to which the ability to fulfill a certain responsibility **depends upon the actions of another component** (interdependence between modules) | **minimize** |

- Good design = **high cohesion, low (loose) coupling**
- With high coupling, a change in one module affects other modules → hard to maintain and reuse

> Exam point: 2024 "(Coupling) and (Cohesion) are two key concepts used to measure design quality… good design = (high) cohesion, (low) coupling", 2023 "Coupling is the degree to which each module (relies/depends) on … (Cohesion) … (minimize) … (maximize)", 2016 "(depends upon) … desirable to (minimize)". Memorize the English definitions word for word.

## Interface and Implementation · Information Hiding {#interface-impl}

- We characterize software components by **what** they can do
- The user of a software component **need only know what it does, not how it does it**
- **Two views of a software system**: interface (edit a recipe, create new recipe, display on terminal) vs implementation (text buffer, window pointer, ingredient list)
- **information hiding**: the **purposeful hiding of implementation details**. A cover keeps you from seeing inside, which also gives **protection**

## Public View and Private View {#public-private}

- **Public view**: those features (data or behavior) that other components can see and use → the interface
- **Private view**: those features (data or behavior) that are used **only within the component** → the implementation
- Distinguishing public and private is a key feature of object-oriented programming (the professor stressed this)

@lesson L3-4 | Formalizing the Interface · Names · Implementation · Integration (Stubs) · Maintenance | L03 p.26–33

## Formalizing the Interface and Choosing Names {#naming}

**5. Formalize the Interface**: formalize the channels of communication between the components
- Identify the general structure of each component. Components with **only one behavior may be made into functions**; components with **many behaviors** are more easily implemented as **classes**
- Give a name to each responsibility → these eventually map onto procedure names. Identify function parameters, assign information to each component, replay the scenarios to ensure all data is available

**Guidelines for selecting names**
- **evocative** (in the context of the problem) — e.g. a name that reveals what is being counted rather than a meaningless name
- **short**
- **pronounceable** (read them out loud)
- **consistent** (within the project; e.g. if you decide variables start lowercase and functions start uppercase, keep it to the end)
- **avoid digits** within a name (count1, count2 tell you nothing about the difference)

> Exam point: 2016 essay "What does 'evocative' mean?" → The name should call to mind (suggest) the meaning/role of the thing in the problem domain.

## Design · Implementation · Unit Testing {#implement}

- **6. Design**: transform the description into a SW layout, design the data structures of each component, transform behavior descriptions into algorithms
- **7. Implementing Components**: implement the desired activities in each component. Components are divided among team members
  - **Unit testing**: subsystems are **validated individually**. Identify the necessary conditions for correct functioning and test with legal input values

## Integration and Stubs {#stub}

**8. Integration of Components**: components are **slowly integrated** into the completed system, using **stubs** for as-yet unimplemented parts
- **stub**: a **simple dummy routine** with no behavior or with very limited behavior. A temporary stand-in for a component not yet developed
- **slowly integrated**: not integrated all at once, but **added one (or a few) at a time and tested** → if a problem appears, the part just added is the cause, so it is easy to find and fix. If everything is integrated at once, you cannot tell where the problem came from
- Errors discovered during integration cause reinvestigation of the validation techniques performed at the subsystem level

> Exam point: 2025·2016 essay "Meaning of 'slowly integrated'? Meaning of 'stubs'?", 2022 blank "(Stub) is a simple dummy routine with no behavior or with very limited behavior".

## Maintenance and Evolution · Common Design Flaws {#maintenance}

**9. Maintenance and Evolution**
- **Software maintenance**: activities **subsequent to the delivery** of the initial working version
- Software does not remain fixed after the first version: bugs are discovered and fixed, requirements change (government regulations, standardization), hardware changes, user expectations change (more features due to competing products), better documentation is required
- **Good design recognizes the inevitability of changes and plans an accommodation for them from the very beginning**
- **Prepare for Change**: predict the most likely sources of change and isolate their effect (interfaces, file formats, communication protocols), isolate interfaces to hardware likely to change, **reduce dependency of one component on another**, record the reasoning behind every major decision in the design documentation

**Common Design Flaws**
- **Direct modification**: directly modifying the data of another component → **a direct violation of encapsulation**
- **Too much responsibility**: difficult to understand and to use
- **No responsibility**: serves no purpose
- **Unused responsibility**: the result of designing components without thinking about how they will be used
- **Misleading names**: names should be short and unambiguously indicate the responsibilities

> Exam point: 2023 blank "(Software maintenance) is the process of changing, modifying, and updating software to keep up with customer needs. (It) is done after the product has launched".
