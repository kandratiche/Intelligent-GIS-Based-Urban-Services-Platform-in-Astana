# Existing System Comparison

## 1. Introduction

The purpose of this comparison is to examine existing systems related to the proposed GIS-based urban-services platform for Astana. The comparison focuses on civic issue reporting, geographic information management, and integration with municipal services.

Four systems or solutions are considered: FixMyStreet, SeeClickFix, ArcGIS Hub, and Open311. They do not provide exactly the same functionality. FixMyStreet and SeeClickFix focus on civic issue reporting, ArcGIS Hub supports geographic data sharing and community engagement, and Open311 is an interoperability standard rather than a complete standalone platform.

The comparison uses common criteria to identify useful features, limitations, and opportunities for the proposed project. Claims about product capabilities should be verified against official documentation before the final submission.

## 2. Comparison Criteria

The systems are compared using the following criteria:

1. Geographic visualization and location-based reporting.
2. Citizen issue submission.
3. Issue categorization and tracking.
4. Integration with municipal workflows.
5. Geographic data sharing and visualization.
6. Support for external integrations or APIs.
7. AI-based report classification.
8. Lost-item matching.
9. Short-term parking prediction.
10. Suitability for adaptation to the Astana use case.

The last three criteria relate directly to the proposed project's modules. A missing feature in the table means that it has not been established as a built-in capability for this comparison; it does not necessarily mean the feature is technically impossible to implement.

## 3. Existing Systems

### 3.1. FixMyStreet

FixMyStreet is a civic reporting platform that allows people to report local problems by identifying their location and describing the issue. Its reporting workflow provides a useful reference for collecting geographic information from citizens.

For the proposed project, FixMyStreet is most relevant to hazard-report submission and location-based categorization. The project may extend this concept by evaluating AI-assisted classification and integrating additional services in one interface.

Official source: https://www.fixmystreet.com/

### 3.2. SeeClickFix

SeeClickFix is a civic engagement and issue-reporting solution that helps residents communicate local problems to public authorities. It is relevant as an example of a workflow connecting public reports and municipal response processes.

For the Astana platform, it provides a comparison point for citizen-facing reporting and service-request management. The exact availability of particular integrations and features depends on the product version and deployment.

Official source: https://seeclickfix.com/

### 3.3. ArcGIS Hub

ArcGIS Hub is a geographic data-sharing and community engagement platform within the ArcGIS ecosystem. It can be used to organize and share data, maps, and information with communities.

It is relevant to the proposed project's GIS interface and the presentation of urban information. However, a geographic data-sharing platform is not automatically equivalent to a civic issue-reporting system or an application that implements the project's three AI modules.

Official source: https://hub.arcgis.com/

### 3.4. Open311

Open311 is an open standard for exchanging information about civic service requests. It is intended to support interoperability between systems that handle municipal service requests.

Unlike the other examples, Open311 is not a complete standalone application. It is included because interoperability may be important if the proposed platform later connects to municipal services or other reporting systems.

Official source: https://www.open311.org/

## 4. Comparative Table

| Criterion | FixMyStreet | SeeClickFix | ArcGIS Hub | Open311 |
|---|---|---|---|---|
| Main purpose | Civic issue reporting | Civic engagement and issue reporting | Geographic data sharing and community engagement | Standard for civic service-request exchange |
| Geographic information | Central to reporting local problems | Used in location-based issue reporting | Central to maps and geographic data | Depends on the systems exchanging requests |
| Citizen issue submission | Core use case | Core use case | Not the primary purpose of Hub itself | Provided by compatible applications, not by the standard alone |
| Issue tracking | Reporting workflow | Reporting and response workflow | Depends on connected applications and data | Depends on implementing systems |
| Municipal workflow integration | Depends on deployment and local arrangements | Depends on product configuration and local arrangements | Can support data sharing; workflow functions depend on connected systems | Designed to support interoperability |
| Geographic data sharing | Not its main purpose | Not its main purpose | Core capability | Not its main purpose |
| External integration | Verify available interfaces for the chosen deployment | Verify available interfaces for the chosen product and plan | Depends on ArcGIS services and configuration | Core purpose is standardized exchange |
| Built-in AI report classification | Not established by this comparison | Not established by this comparison | Not established as a core Hub function | Not provided by the standard itself |
| Built-in lost-item matching | Not established by this comparison | Not established by this comparison | Not established by this comparison | Not provided by the standard itself |
| Built-in parking prediction | Not established by this comparison | Not established by this comparison | Not established by this comparison | Not provided by the standard itself |
| Relevance to Astana | Reference for citizen hazard reports | Reference for citizen reporting and service workflows | Reference for GIS and urban data presentation | Reference for future municipal-system interoperability |

## 5. Analysis

The comparison shows that the selected systems address different parts of the proposed platform's requirements.

FixMyStreet and SeeClickFix provide the closest conceptual comparisons for citizen-facing issue reporting. Their workflows can inform how residents describe a problem, specify a location, and follow the handling of a report.

ArcGIS Hub is more relevant to geographic data organization, mapping, and information sharing. It illustrates the value of a geographic interface but should not be treated as a direct substitute for all service workflows.

Open311 addresses a different layer of the problem: interoperability. It can inform future integration with compatible municipal systems, but it does not itself supply a complete user interface or implement the proposed AI modules.

None of these four systems has been established by this comparison as providing all three of the proposed modules together: hazard-report classification, lost-item matching, and short-term parking prediction. This is a scoped finding based on the selected systems and the information documented here, not proof that no comparable platform exists anywhere.

## 6. Why the Proposed Solution Is Needed

The proposed GIS-based urban-services platform aims to bring several workflows into one prototype for the Astana use case:

- Hazard-report classification to organize citizen-submitted reports for further review.
- Lost-item matching to identify potentially related records.
- Short-term parking prediction based on an explicitly defined dataset and prediction target.
- A common geographic interface for presenting relevant information.

The comparison suggests that existing solutions provide useful references for individual aspects of the project, including citizen reporting, geographic data sharing, and service-request interoperability. The proposed contribution is to integrate the selected workflows in one prototype and evaluate their technical behavior and usability.

This does not imply that existing systems are generally inadequate. Their suitability depends on the intended users, deployment context, available integrations, and project requirements. The prototype should be evaluated against clearly defined criteria rather than assuming that combining features automatically produces a better service.

## 7. Limitations of the Comparison

This comparison is a preliminary feature-level review. It is based on the general purposes of the selected systems and does not constitute a hands-on benchmark or a complete audit of current product features.

Before final submission, the team should verify each product-specific claim using current official documentation, API references, and available demonstrations. If screenshots or test results are required as evidence, they should be collected directly from the relevant official websites or working systems.

Feature availability may depend on subscription level, configuration, geographic coverage, or deployment. Open311 is a standard rather than a standalone product, so it should not be evaluated as if it were equivalent to the three applications.

## 8. Conclusion

The four selected systems provide complementary points of comparison. FixMyStreet and SeeClickFix illustrate citizen issue reporting, ArcGIS Hub illustrates geographic data sharing, and Open311 illustrates standardized exchange of municipal service requests.

The proposed Astana platform focuses on integrating hazard-report classification, lost-item matching, and short-term parking prediction within one GIS-based prototype. The comparison provides a starting point for identifying requirements and evaluating the proposed solution, while further verification of current features and evidence is needed before making definitive claims about competing systems.

## References

1. FixMyStreet. Official website. https://www.fixmystreet.com/
2. SeeClickFix. Official website. https://seeclickfix.com/
3. ArcGIS Hub. Official website. https://hub.arcgis.com/
4. Open311. Official website. https://www.open311.org/