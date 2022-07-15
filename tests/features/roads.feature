Feature: Roads

  Scenario: Building a Road between two Towns
  
    Given: a town exists
    And: a charcater is located within the town
    And: another town exists within the same region or a connected region
    And: the charcater has the required building materials
    And: the charcater has enough worker robots
    When: the build road command is used
    And: the target is the second town
    Then: road construction begins
