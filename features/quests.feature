Feature: Quests

  Scenario: First Quest
    Given a new character has been created
    When the quest command is used
    Then a list of available quests is shown
    
