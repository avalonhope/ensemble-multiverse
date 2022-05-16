Feature: biospheres

  Scenario: growing plants
    Given the planet has an athmosphere
    And there is enough sunlight
    And there is enough water
    And there is enough oxygen
    And the temperature is not too high
    And the temperature is not too low
    When plants grow
    Then they produce oxygen
    And they consume nutrients
    
