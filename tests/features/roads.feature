Feature: Roads

  Scenario: Building a Road between two Towns
  
    Given: a town exists
    And: a character is located within the town
    And: another town exists within the same region or a connected region
    And: the character has the required building materials
    And: the character has enough worker robots
    When: the build road command is used
    And: the target is the second town
    Then: road construction begins
