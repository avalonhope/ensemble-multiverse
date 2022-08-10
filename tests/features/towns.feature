Feature: Towns

  Scenario: Zones
    Given a character is located within a town
    When the zones command is used
    Then a list of zones within the town is shown
    
 Scenario: Roads
   Given a character is located within a town
   When the roads command is used
   Then a list of roads out of town is shown

 Scenario: Travel with a Vehicle
   Given a charcater is located within a town
   And the charcater is onboard a vehicle
   And the charcater has control of the vehicle
   When the travel command is used
   And a road is specified
   Then the vehicle enters that road
   
