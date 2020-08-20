Title: Robot Framework - dostęp do ostatniego elementu listy
Date: 2019-06-05 13:07
Author: filipgorczynski
Category: Programowanie
Slug: robot-framework-dostep-do-ostatniego-elementu-listy
Status: draft

```

    ${available_terms}=     Set Variable                ${first_plan.find_elements_by_css_selector('.multiselect-term-selector .multiselect__element')}
    ${number_of_terms}=     Get Length                  ${available_terms}

    # Click on the last available term
    ${last_element_index}=  Evaluate                    ${number_of_terms} - 1
    Click Element                                       ${available_terms}[${last_element_index}]

    ```
