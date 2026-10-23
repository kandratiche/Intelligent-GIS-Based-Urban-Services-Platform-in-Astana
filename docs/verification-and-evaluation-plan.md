# Verification and Evaluation Plan

## 1. Purpose

This document defines how the Intelligent GIS-Based Urban Services Platform for Astana will be verified and evaluated. The purpose is to check whether the implemented prototype satisfies its requirements, produces appropriate outputs, and provides understandable workflows for users.

The planned prototype contains three main AI-supported modules:

1. Hazard-report classification.
2. Lost-item matching.
3. Short-term parking prediction.

The platform also provides a common GIS-based interface for presenting urban-service information. Testing will cover both individual modules and the integrated application.

The tests described below are planned activities. Their results must be recorded after implementation and must not be reported as completed before testing has taken place.

## 2. Verification Objectives

The verification process has the following objectives:

- Confirm that implemented functions behave according to the project requirements.
- Check the correctness of report classification and lost-item matching.
- Measure the prediction performance of the parking module.
- Verify that geographic information is displayed and handled correctly.
- Evaluate the usability and clarity of the main user workflows.
- Identify defects, limitations, and improvements required before the final demonstration.

## 3. Test Types

### 3.1. Functional Testing

Functional testing will verify that each implemented feature behaves as expected. Test cases will cover input validation, report submission, category assignment, candidate matching, parking predictions, and display of results on the map.

### 3.2. Integration Testing

Integration testing will examine whether the GIS interface, data storage, and analytical modules work together. Tests will check that data are passed correctly between components and that errors in one component do not silently produce misleading results in another.

### 3.3. AI Module Evaluation

Each AI-supported module will be evaluated independently using labelled test examples or an appropriate reference dataset. The evaluation method will depend on the implemented algorithm and the availability of suitable data.

### 3.4. Usability Testing

Usability testing will assess whether intended users can understand the interface and complete representative tasks. Participants should receive consistent task instructions, and observations should be recorded using a predefined procedure.

### 3.5. Reliability and Error Handling

Reliability checks will examine how the prototype responds to missing fields, invalid inputs, unavailable data, and other expected error conditions. The system should provide clear feedback instead of presenting invalid results as successful outputs.

## 4. Evaluation Metrics

### 4.1. Hazard-Report Classification

The classification module will be evaluated using a labelled test set containing hazard reports and their reference categories.

The main metrics will be:

- **Accuracy:** proportion of reports assigned the correct category.
- **Precision:** proportion of reports assigned to a category that truly belong to that category.
- **Recall:** proportion of reports in a category that are successfully identified.
- **Macro-F1:** average F1 score across categories, giving each category equal weight.

The confusion matrix will also be inspected to identify categories that are frequently confused. If the dataset is small or imbalanced, the results will be interpreted cautiously.

### 4.2. Lost-Item Matching

The lost-item matching module will be evaluated using example pairs of reports labelled as matches or non-matches.

The proposed metrics are:

- **Precision@k:** proportion of the top-k suggested candidates that are valid matches.
- **Recall@k:** proportion of known valid matches retrieved within the top-k candidates.
- **Top-1 accuracy:** proportion of test cases in which the first suggested candidate is a valid match, when a single reference match is available.

The value of k and the definition of a valid match must be fixed before testing. If the prototype does not produce ranked candidates, the metrics must be adapted to its actual output.

### 4.3. Short-Term Parking Prediction

The parking module will be evaluated against observed or reference parking values for a predefined prediction horizon.

The proposed metrics are:

- **Mean Absolute Error (MAE):** average absolute difference between predicted and observed values.
- **Root Mean Squared Error (RMSE):** square root of the average squared prediction error.
- **Baseline improvement:** difference between the proposed model's error and the error of a simple baseline model.

The prediction target must be specified clearly, for example, occupancy level or availability count. MAE and RMSE should only be used when the target is numeric.

### 4.4. Usability

Usability evaluation will use a small set of representative tasks, such as submitting a hazard report, locating a potentially matching lost-item report, and viewing a parking prediction.

The following measures will be recorded:

- Task completion rate.
- Time required to complete each task.
- Number and type of user errors.
- Participant feedback on clarity and ease of use.

The number of participants and the task procedure should be documented in the final report. A small academic evaluation should not be presented as representative of all city residents.

### 4.5. Functional and Integration Tests

Functional and integration tests will use pass/fail outcomes based on predefined expected behavior. The report will record the number of tests passed, the number failed, the test environment, and any unresolved defects.

## 5. Baseline Solutions

Each analytical module should be compared against a simple, transparent baseline.

| Module | Proposed approach | Baseline for comparison | Purpose |
|---|---|---|---|
| Hazard-report classification | Implemented classification method | Majority-class prediction or a simple rule-based classifier | Determine whether the selected method improves on a simple alternative |
| Lost-item matching | Implemented matching or ranking method | Keyword overlap or another simple, deterministic matching rule | Determine whether the selected method retrieves better candidate matches |
| Parking prediction | Implemented prediction method | Persistence forecast, using the most recent observed value, where appropriate | Determine whether the model improves on a simple forecast |

The baseline must be appropriate to the available dataset and the implemented system. If the proposed module uses a different type of output, its baseline and metrics must be adapted accordingly.

## 6. Measurement Conditions

To make the evaluation reproducible, the following conditions will be documented:

- Software version and execution environment.
- Dataset source, size, format, and collection period where known.
- Data cleaning and preprocessing procedures.
- Training, validation, and test split, where model training is required.
- Random seed and relevant model settings, where applicable.
- Definition of labels, valid matches, and prediction targets.
- Metrics and baseline methods used for each module.
- Test date, test procedure, observed results, and known limitations.

Test data must be separated appropriately from training data to reduce the risk of data leakage. For time-dependent parking prediction, the split should respect time order where feasible.

If real Astana municipal datasets are unavailable, the prototype may use clearly documented sample or synthetic data. In that case, the evaluation must explicitly state that its findings do not establish real-world performance under live city conditions.

## 7. Requirements-to-Test Mapping

The following table maps the main project functions to the proposed verification activities. The identifiers are provisional and should be aligned with the final requirements specification.

| Requirement ID | Requirement or capability | Verification method | Evidence to collect | Success condition |
|---|---|---|---|---|
| REQ-GIS-01 | Display relevant urban-service information geographically | Functional test | Screenshot and test record | Relevant records appear at the expected locations |
| REQ-HAZ-01 | Classify submitted hazard reports | Labelled test-set evaluation | Reference labels, predictions, metrics | Results are measured and reported against the predefined baseline |
| REQ-LOST-01 | Retrieve potentially matching lost-item reports | Matching evaluation | Test pairs, ranked results, Precision@k or another suitable metric | Matching behavior is measured using predefined criteria |
| REQ-PARK-01 | Produce short-term parking predictions | Prediction evaluation | Reference values, predictions, MAE/RMSE where applicable | Prediction error is measured against the predefined baseline |
| REQ-INT-01 | Connect the interface and analytical modules | Integration testing | Test cases and pass/fail records | Data are passed correctly between the implemented components |
| REQ-USE-01 | Support understandable user workflows | Usability testing | Task completion, time, errors, participant feedback | Usability observations are recorded and assessed against predefined criteria |
| REQ-ERR-01 | Handle invalid or incomplete inputs | Negative functional tests | Input examples and observed responses | Invalid input produces clear feedback and does not silently create misleading results |

These provisional identifiers must not replace the official IDs if the project's requirements specification already defines them.

## 8. Test Execution Procedure

Testing will follow these steps:

1. Confirm which features are implemented and identify the version under test.
2. Prepare the datasets, reference labels, and test cases.
3. Define metrics, baselines, and success criteria before running the evaluation.
4. Run functional and integration tests.
5. Evaluate each analytical module using its own test data and metrics.
6. Conduct usability tasks if participants and suitable arrangements are available.
7. Record results, failures, limitations, and screenshots or other evidence.
8. Compare observed results with the predefined criteria.
9. Document unresolved issues and identify possible improvements.

Any changes to the model, data, or evaluation procedure should be recorded so that the reported results can be interpreted correctly.

## 9. Results and Reporting Template

The following table should be completed after tests have actually been executed.

| Test or module | Dataset or test cases | Metric | Baseline result | Proposed solution result | Outcome and notes |
|---|---|---|---|---|---|
| Hazard classification | To be recorded | Accuracy, macro-F1 | To be measured | To be measured | Pending |
| Lost-item matching | To be recorded | Precision@k or suitable alternative | To be measured | To be measured | Pending |
| Parking prediction | To be recorded | MAE/RMSE where applicable | To be measured | To be measured | Pending |
| Functional tests | To be recorded | Pass/fail count | Not applicable | To be measured | Pending |
| Integration tests | To be recorded | Pass/fail count | Not applicable | To be measured | Pending |
| Usability tests | To be recorded | Completion, time, errors, feedback | Not applicable | To be measured | Pending |

No numerical results should be inserted until they have been obtained from actual tests.

## 10. Limitations and Risks

The quality of the evaluation will depend on data availability, data quality, representative test cases, and the maturity of the prototype. A small or synthetic dataset may not reflect real city conditions. Incomplete reference labels may also limit the interpretation of classification and matching metrics.

Parking prediction requires an explicitly defined target and suitable reference observations. Usability results from a small group of participants will provide preliminary feedback rather than a city-wide assessment.

The final evaluation report should describe these limitations and avoid claiming that the prototype is ready for live municipal deployment unless that level of validation has actually been performed.

## 11. Conclusion

This plan defines a structured approach for verifying the GIS-based urban-services prototype and evaluating its three proposed analytical modules. It combines functional and integration testing with module-specific metrics, baseline comparisons, measurement conditions, and usability evaluation.

The final evidence will consist of documented test cases, measured results, baseline comparisons, and a mapping between requirements and verification activities. This will allow the project team to assess what has been demonstrated, identify remaining limitations, and make evidence-based conclusions about the prototype.