Title: Robot Framework - dobieranie się do elementów potomnych z obiektu WebElement
Date: 2019-06-05 13:06
Author: filipgorczynski
Category: Tech
Slug: robot-framework-dobieranie-sie-do-elementow-potomnych-z-obiektu-webelement
Status: draft

```

    # Huurrraaaay!! https://seleniumhq.github.io/selenium/docs/api/py/webdriver_remote/selenium.webdriver.remote.webelement.html
    # Name of the first Protection Plan
    ${selected_protection_plan_name}=   Set Variable    ${first_plan.find_element_by_css_selector('.plan-name strong').text}

    Wait Until Element Does Not Contain                 css:.p_payment-repr         ${basic_price}          timeout=30
    ${price_with_protection_plan}=   Get Text                        css:.p_payment-repr
    Should Not Be Equal                                 ${basic_price}              ${price_with_protection_plan}

    Click Element                                       ${first_plan.find_element_by_css_selector('.multiselect__tags')}
    Wait Until Element Is Visible                       ${first_plan.find_element_by_css_selector('.multiselect-term-selector')}

    ${available_terms}=     Set Variable                ${first_plan.find_elements_by_css_selector('.multiselect-term-selector .multiselect__element')}
    ${number_of_terms}=     Get Length                  ${available_terms}
    ```
