.. _changelog:

Changelog
=========

`trunk (saas-2)`
----------------

- Stage/state update

  - ``thmdocument.task``: removed inheritance from ``base_stage`` class and removed
    ``state`` field. Added ``date_last_stage_update`` field holding last stage_id
    modification. Updated reports.
  - ``thmdocument.task.type``: removed ``state`` field.

- Removed ``thmdocument.task.reevaluate`` wizard.
