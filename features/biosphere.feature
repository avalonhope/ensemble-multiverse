Feature: biospheres

  Scenario: growing plants
    Given there is a planet
    And the planet has an athmosphere
    And there is enough sunlight
    And there is enough water
    And there is enough oxygen
    And there is not too much oxygen
    And the temperature is not too high
    And the temperature is not too low
    And some aquatic plants already exist
    And there are enough nutrients
    When aquatic plants grow
    Then they produce oxygen
    And they consume nutrients
    
Scenario: microbes
  Given there is a planet
    And the planet has an athmosphere
    And there is enough sunlight
    And there is enough water
    And there is enough oxygen
    And there is not too much oxygen
    And the temperature is not too high
    And the temperature is not too low
    And some microrobes already exist
    When microbes grow
    Then they produce nutrients
