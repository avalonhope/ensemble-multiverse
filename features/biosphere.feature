Feature: biospheres

  Scenario: growing plants
    Given there is a planet
    And the planet has an athmosphere
    And the planet has enough sunlight
    And the planet has enough water
    And the planet has enough oxygen
    But the planet does hot have too much oxygen
    And the average planetary temperature is not too high for plants
    And the average planetary temperature is not too low for plants
    And some aquatic plants already exist in the biosphere
    And there are enough nutrients in the biosphere
    When aquatic plants grow
    Then they produce oxygen
    And they consume nutrients
    
Scenario: microbes
  Given there is a planet
    And the planet has an athmosphere
    And the planet has enough sunlight
    And the planet has enough water
    And the planet has enough oxygen
    But the planet does not have too much oxygen
    And the temperature is not too high for microbes
    And the temperature is not too low for microbes
    And some microrobes already exist
    When microbes grow
    Then they produce nutrients
