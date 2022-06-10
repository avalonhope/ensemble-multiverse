Feature: Quests

  Scenario: First Quest
    Given a character exists
    When the quests command is used
    Then a list of available quests is shown
    
  Scenario: Join Quest
    Given a character exists
    And a quest exists
    When the joinquest command is used
    Then the character is added to the list of quest participants
  
  Scenario: Multi-User Quest
    Given a character exists
    And a quest exists
    And the quest has an existing partipant
    When the joinquest command is used
    Then the character is added to the list of quest participants
