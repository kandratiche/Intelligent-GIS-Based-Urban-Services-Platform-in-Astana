# Literature Review: GIS-Based Smart City Platforms and AI-Enhanced Urban Services

## 1. Introduction

Smart-city platforms combine urban data, digital services, and analytical methods to help people and public organizations understand and respond to city needs. The bibliography prepared for this project covers several relevant strands: Internet of Things (IoT) and machine learning in smart cities, urban digital twins, crowdsourced citizen information, smart parking, lost-item search, security and privacy, and citizen acceptance of digital services.

The proposed project is an intelligent GIS-based urban-services platform for Astana. Its intended prototype brings together three functions: classification of hazard reports, matching of lost-item reports, and short-term parking prediction. The reviewed literature provides context for these functions and for broader design considerations such as data integration, public participation, security, and usability.

This review synthesizes the records in the project's `GIS_Smart_City_References.bib` bibliography. The comparison below is based on the bibliographic information and the research focus indicated by each publication's title and publication type. Before final submission, the team should consult the full text of each selected paper to confirm detailed methods, findings, and limitations.

## 2. Review Scope and Method

The bibliography contains journal articles and reviews published between 2021 and 2024. It covers the following themes:

- Smart-city IoT, machine learning, and context-aware services.
- Smart parking architectures, scheduling, security, and urban viability.
- Crowdsourcing, volunteered geographic information, and public-safety reporting.
- Lost-item search systems and recommendation methods.
- Urban digital twins and their integration challenges.
- Security, privacy, citizen acceptance, and citizen discontent in smart-city services.

The sources are grouped thematically and compared by focus, approach as indicated by the publication, project-relevant contribution, and implementation consideration. This is a focused narrative review of the supplied bibliography, not a claim to have performed an independent systematic database search. A reproducible systematic review would additionally require documented databases, search strings, screening criteria, and a record of excluded papers.

## 3. Review of Existing Research

### 3.1. Smart-City Platforms, IoT, and Machine Learning

Heidari et al. (2022) review machine-learning and deep-learning applications in smart cities and societies based on IoT, while Rocha et al. (2022) review context-awareness applications supported by smart-city infrastructure. Together, these topics are relevant to platforms that use data from different sources to provide services adapted to a situation or location. The practical implication for this project is to define what data each module needs, how often it is updated, and what output is useful to the user.

Smart-city systems are not solely technical deployments. Bestepe and Özkan Yıldırım (2022) study acceptance of IoT-based and sustainability-oriented smart-city services using a mixed-methods approach, and van Twist et al. (2023) review literature on citizen discontent with smart cities. These topics signal that adoption, trust, and public concerns should be considered alongside technical functionality. For the Astana prototype, user-oriented evaluation should therefore consider whether users understand the results and find the workflows useful, rather than measuring only whether the application runs.

### 3.2. Smart Parking and Urban Mobility

The bibliography includes several different perspectives on smart parking. Floris et al. (2022) describe a Social IoT-based platform for deploying a smart-parking solution. Veeramanickam et al. (2022) focus on an IoT parking model using Arduino UNO and first-come, first-served priority scheduling. Singh et al. (2022) address a blockchain-enabled secure framework for energy-efficient smart parking. Lee et al. (2022) review edge-computing-enabled secure and energy-efficient smart parking, while Muzzini et al. (2023) examine smart parking in relation to urban viability.

These publications show that “smart parking” can refer to several distinct problems: detecting or sharing availability, scheduling access, supporting secure data exchange, processing data near devices, or improving urban outcomes. They should not be treated as interchangeable methods. The proposed project focuses specifically on short-term parking prediction; consequently, its evaluation must define the prediction target, forecast horizon, input data, and comparison baseline. The cited parking papers provide design context, but the bibliography alone does not establish that any one architecture or algorithm is best for Astana.

### 3.3. Crowdsourcing, Citizen Reports, and Geographic Information

Currin et al. (2022) examine participatory crowdsourcing of public-safety reports in South Africa. Jiang et al. (2023) provide a bibliometric and scientometric review of crowdsourcing research in smart cities. Tzavella et al. (2024) review volunteered geographic information in crisis, emergency, and disaster management. Schrammeijer et al. (2021) study crowdsourcing citizens' preferences for urban green spaces to inform needs-based management decisions.

This strand is relevant to a platform that accepts citizen-submitted hazard reports. It suggests that reports can be a source of locally generated information, while also raising practical questions about completeness, quality, representativeness, location accuracy, and how reports are reviewed. Automated classification should therefore support triage rather than be presented as a definitive safety decision. The project should document how test reports are labelled and evaluate whether categories are assigned correctly.

### 3.4. Lost-Item Search and Recommendation

Zhou et al. (2024) present *LostNet: A smart way for lost and find*, and Solovei and Vorochek (2024) describe the development of a software system for searching for lost items. Zhang et al. (2022) examine a three-way Naive Bayesian collaborative-filtering recommendation model for smart cities. These sources relate to the problem of identifying potentially relevant connections between user-provided records.

For the proposed lost-item matching module, relevant information may include text descriptions, categories, dates, and locations, depending on what the prototype actually collects. Matching results should be shown as potential matches rather than confirmed identities. The system should be evaluated on labelled example pairs, including both relevant matches and non-matches, and should explain the criteria used to rank candidates. Detailed claims about the algorithms or measured performance in the cited papers should be added only after checking their full texts.

### 3.5. Urban Digital Twins and Integration Challenges

Weil et al. (2023) provide a systematic review of urban digital-twin challenges, and Mazzetto (2024) reviews urban digital-twin integration, challenges, and future directions. These publications are relevant to the broader question of integrating spatial data, digital representations, and analytical functions in a smart-city environment.

A full urban digital twin can involve more than a map-based application: depending on its definition and implementation, it may require connected data sources, synchronization with real-world conditions, and validated models. The proposed project should therefore be described according to what is actually implemented. Unless real-time synchronization and a corresponding digital representation are built and evaluated, “GIS-based urban-service prototype” is a more defensible description than “complete digital twin.”

### 3.6. Security, Privacy, and Location Prediction

Rizi and Hosseini Seno (2022) systematically review technologies and solutions for improving security and privacy protection in smart cities. Chekol and Fufa (2022) survey next-location prediction techniques, applications, and challenges. Singh et al. (2022) and Lee et al. (2022) also address security in the smart-parking context.

Location data and citizen reports can be sensitive, especially when they describe incidents, movements, or personal belongings. The platform should collect only information necessary for its intended functions, avoid exposing personal details unnecessarily, and make clear how sample or real user data are handled. Next-location prediction is adjacent to spatial prediction, but it should not be presented as equivalent to parking-availability forecasting: the target, data, and evaluation procedure are different.

## 4. Comparative Analysis of Selected Studies

The following table covers the records in the supplied bibliography. “Project relevance” and “implementation consideration” are interpretations for this project based on the stated publication focus; they are not substitutes for reading the full papers.

| Source and year | Focus and approach indicated by the source | Contribution to the project context | Limitations or implementation considerations | Relevance to our project |
|---|---|---|---|---|
| Floris et al. (2022) | Social IoT-based smart-parking platform | Provides an architectural perspective on connected parking services | A platform architecture may depend on connected data sources and infrastructure not available in a prototype | Parking module design and possible future sensor integration |
| Veeramanickam et al. (2022) | IoT smart-parking model using Arduino UNO and FCFS scheduling | Illustrates a device-oriented parking model and a defined scheduling approach | Hardware-based detection and FCFS scheduling do not by themselves establish predictive accuracy | Helps distinguish parking occupancy detection from prediction |
| Singh et al. (2022) | Blockchain-enabled secure and energy-efficient smart parking | Highlights security and energy-efficiency considerations in parking systems | Blockchain can add implementation complexity and may not be necessary for a small prototype | Security considerations for future parking-system extensions |
| Muzzini et al. (2023) | Smart parking and urban viability | Connects parking solutions with broader urban outcomes | Urban viability depends on local context and evaluation criteria | Helps explain the practical importance of parking services |
| Schrammeijer et al. (2021) | Crowdsourcing citizens' urban green-space preferences | Illustrates how citizen input can inform urban management | Preferences collected from participants may not represent the entire population | General lessons for citizen participation and report collection |
| Currin et al. (2022) | Participatory crowdsourcing of public-safety reports | Directly relates to citizen-generated safety information | Report quality, completeness, and the local context affect usefulness | Hazard-report collection and classification |
| Zhou et al. (2024) | Lost-item search system, *LostNet* | Provides a directly relevant example of a digital lost-and-found service | Detailed method and performance claims should be checked against the full paper | Lost-item matching module |
| Solovei and Vorochek (2024) | Software system for searching for lost items | Provides another example of a lost-item search application | The bibliographic record alone does not establish how well its method transfers to the proposed platform | Requirements and workflow design for lost-item search |
| Bestepe and Özkan Yıldırım (2022) | Mixed-methods study of acceptance of IoT-based smart-city services | Emphasizes the importance of user acceptance | Acceptance findings may depend on participants and service context | User-experience and acceptance evaluation |
| Zhang et al. (2022) | Three-way Naive Bayesian collaborative-filtering recommendation model | Provides an example of a recommendation approach in a smart-city context | A recommendation method is not automatically suitable for matching lost-item reports | Background for comparing possible matching approaches |
| Lee et al. (2022) | Review of edge-computing-enabled secure and energy-efficient smart parking | Summarizes parking-system design concerns involving edge computing, security, and energy use | Edge infrastructure may be outside the scope of the prototype | Future architecture considerations for parking |
| Rocha et al. (2022) | Systematic review of context-awareness applications supported by smart-city infrastructure | Provides context on services that use urban infrastructure and contextual information | Applications and infrastructures may differ substantially between cities | Location-aware service design |
| Tzavella et al. (2024) | Scoping review of volunteered geographic information in crisis and disaster management | Explores geographic information contributed by volunteers in emergency contexts | Crowdsourced information can be uneven in quality and spatial coverage | Geographic citizen reports and hazard-report workflows |
| Jiang et al. (2023) | Bibliometric and scientometric review of crowdsourcing in smart cities | Maps research themes in smart-city crowdsourcing | A bibliometric review does not itself validate a particular report-classification system | Background for citizen-report collection |
| Rizi and Hosseini Seno (2022) | Systematic review of smart-city security and privacy technologies | Identifies security and privacy as important smart-city concerns | The appropriate controls depend on the data and threat model of the actual platform | Privacy-aware handling of citizen and location data |
| Chekol and Fufa (2022) | Survey of next-location prediction techniques | Provides background on prediction using location-related data | Predicting a person's next location differs from predicting parking availability | Related spatial-prediction concepts, with a clearly defined distinction |
| Heidari et al. (2022) | Systematic review of machine learning and deep learning in IoT-based smart cities | Provides broad context for AI methods in smart-city systems | Broad reviews do not select or validate the best method for this particular dataset | Background for the platform's AI modules |
| Weil et al. (2023) | Systematic review of urban digital-twin challenges | Summarizes challenges involved in urban digital twins | Full digital-twin implementation may require extensive integration and ongoing data synchronization | Helps define a realistic prototype scope |
| Mazzetto (2024) | Review of urban digital-twin integration, challenges, and future directions | Provides context for integration in smart-city development | Findings need to be translated into requirements appropriate to the proposed system | Data integration and future platform architecture |
| van Twist et al. (2023) | Systematic review of citizen discontent with smart cities | Highlights concerns and negative reactions associated with smart-city initiatives | General findings may not predict reactions to a specific local prototype | User feedback, transparency, and usability considerations |

The table shows that the bibliography covers different parts of the project problem. Some studies address smart-parking architectures, while others focus on prediction, citizen reports, lost-item search, security, or public acceptance. Their methods and findings should not be treated as directly comparable because the research questions differ.

The proposed project builds on these complementary topics rather than claiming to introduce an entirely new GIS or AI methodology.

## 5. Critical Synthesis

Four recurring themes emerge from the supplied bibliography.

First, integration is important. Smart-city services can depend on data from sensors, public organizations, geographic datasets, and citizen reports. These sources may differ in format, quality, update frequency, and spatial accuracy. The platform should therefore define how data are structured, validated, and presented.

Second, AI functions require separate evaluation. Hazard-report classification, lost-item matching, and parking prediction are different tasks. Each needs its own input definition, test data, baseline, and evaluation metrics. A single claim that “AI works” would not be sufficient evidence for all three.

Third, public-facing services require attention to privacy, security, and user acceptance. The literature in the supplied bibliography includes explicit work on smart-city privacy, security, acceptance, and citizen discontent. These topics support including usability and responsible data handling in the project evaluation.

Fourth, smart parking and urban digital twins span a wide range of technical ambitions. Sensor networks, edge computing, blockchain, and full digital-twin capabilities may be relevant to some systems, but they should not be added to this project without a clear need and feasible data. The prototype should prioritize the functions that can be implemented and evaluated within its actual scope.

## 6. Research Gap

The supplied bibliography covers several related areas, including crowdsourced public-safety reports, lost-item search, smart parking, smart-city AI, data integration, privacy, and user acceptance. These publications provide separate perspectives on relevant components and concerns.

The project-specific gap motivating this work is the need to design and evaluate a single GIS-based prototype for the Astana use case that brings several urban-service workflows together through a common interface. The proposed prototype focuses on:

1. **Hazard-report classification:** organizing submitted reports into categories to support human review.
2. **Lost-item matching:** identifying potentially related lost-item records using the information available in the prototype.
3. **Short-term parking prediction:** estimating parking conditions from a defined historical or sample dataset.

The proposed contribution is the integration of these functions within one platform and the evaluation of their technical behavior and usability in the intended use case. This is a project-specific motivation, not proof that no comparable system exists. A stronger novelty claim would require a documented comparison with existing platforms and implementations.

## 7. Relevance to the Proposed Astana Platform

The bibliography informs several design and evaluation decisions:

- **Common spatial interface:** use GIS to present reports and parking information in their geographic context.
- **Separate module evaluation:** define distinct test cases and metrics for classification, matching, and prediction.
- **Citizen-report quality:** consider incomplete, inaccurate, duplicated, or outdated reports and provide a review workflow.
- **Privacy and security:** limit collected personal information and avoid exposing sensitive location or report details unnecessarily.
- **User-oriented evaluation:** assess whether users understand the interface, interpret results correctly, and find the workflows useful.
- **Feasible scope:** distinguish functions implemented in the prototype from possible future extensions such as live IoT integration, edge computing, blockchain, or a full urban digital twin.

These are design implications drawn from the themes represented in the bibliography. Specific requirements should be finalized alongside the project's requirements specification and verification plan.

## 8. Limitations of This Review

This draft is based on the bibliographic records supplied in `GIS_Smart_City_References.bib`. The comparison uses each record's title, publication type, and bibliographic metadata to organize the literature. It does not claim that the full text of every article has been examined or that detailed findings and experimental results have been independently verified.

Before final submission, the team should read the full text of the most relevant papers, record their actual methods and findings, check that all bibliographic details are correct, and add any required sources missing from the bibliography. The supplied list should be checked against the expected number of publications. The review also does not document a complete database search and screening process; it should therefore be described as a focused narrative review unless that process is completed.

## 9. Conclusion

The supplied bibliography covers smart-city IoT and AI, parking systems, crowdsourced geographic information, public-safety reports, lost-item search, urban digital twins, security and privacy, and citizen acceptance. Together, these areas provide relevant background for a GIS-based urban-services prototype, while also showing that the project's modules and evaluation questions must be defined separately.

For the Astana use case, the prototype aims to integrate hazard-report classification, lost-item matching, and short-term parking prediction through a common geographic interface. The project's contribution should be assessed through module-specific technical tests and user-oriented evaluation. Its claims should remain proportional to the functions, data, and validation actually implemented.

## References

1. Floris, A., Porcu, S., Atzori, L., & Girau, R. (2022). A Social IoT-based platform for the deployment of a smart parking solution. *Computer Networks, 205*, 108756. https://doi.org/10.1016/j.comnet.2021.108756

2. Veeramanickam, M. R. M., Venkatesh, B., Bewoor, L. A., Bhowte, Y. W., Moholkar, K., & Bangare, J. L. (2022). IoT based smart parking model using Arduino UNO with FCFS priority scheduling. *Measurement: Sensors, 24*, 100524. https://doi.org/10.1016/j.measen.2022.100524

3. Singh, S. K., Pan, Y., & Park, J. T. (2022). Blockchain-enabled secure framework for energy-efficient smart parking in sustainable city environment. *Sustainable Cities and Society, 76*, 103364. https://doi.org/10.1016/j.scs.2021.103364

4. Muzzini, F., Capodieci, N., & Montangero, M. (2023). Improving urban viability through smart parking. *International Journal of Parallel, Emergent and Distributed Systems, 38*(6), 522–540. https://doi.org/10.1080/17445760.2023.2246166

5. Schrammeijer, E. A., van Zanten, B. T., & Verburg, P. H. (2021). Whose park? Crowdsourcing citizens' urban green space preferences to inform needs-based management decisions. *Sustainable Cities and Society, 74*, 103249. https://doi.org/10.1016/j.scs.2021.103249

6. Currin, A., Flowerday, S., de la Rey, E., van der Schyff, K., & Foster, G. (2022). A smart city qualitative data analysis model: Participatory crowdsourcing of public safety reports in South Africa. *The Electronic Journal of Information Systems in Developing Countries, 88*(6), e12232. https://doi.org/10.1002/isd2.12232

7. Zhou, M., Fung, I., Yang, L., Wan, N., Di, K., & Wang, T. (2024). LostNet: A smart way for lost and find. *PLOS ONE, 19*(10), e0310998. https://doi.org/10.1371/journal.pone.0310998

8. Solovei, I., & Vorochek, O. (2024). Development of a software system for searching for lost items. *Municipal Economy of Cities, 3*(184), 2–9. https://doi.org/10.33042/2522-1809-2024-3-184-2-9

9. Bestepe, F., & Özkan Yıldırım, S. (2022). Acceptance of IoT-based and sustainability-oriented smart city services: A mixed methods study. *Sustainable Cities and Society, 80*, 103794. https://doi.org/10.1016/j.scs.2022.103794

10. Zhang, C., Duan, X., Liu, F., Li, X., et al. (2022). Three-way Naive Bayesian collaborative filtering recommendation model for smart city. *Sustainable Cities and Society, 76*, 103373. https://doi.org/10.1016/j.scs.2021.103373

11. Lee, C. P., Leng, F. T. J., Habeeb, R. A. A., Amanullah, M. A., & ur Rehman, M. H. (2022). Edge computing-enabled secure and energy-efficient smart parking: A review. *Microprocessors and Microsystems, 93*, 104612. https://doi.org/10.1016/j.micpro.2022.104612

12. Rocha, N. P., Dias, A., Santinha, G., Rodrigues, M., Rodrigues, C., Queirós, A., Bastardo, R., & Pavão, J. (2022). Systematic literature review of context-awareness applications supported by smart cities' infrastructures. *SN Applied Sciences, 4*, 90. https://doi.org/10.1007/s42452-022-04979-0

13. Tzavella, K., Skopeliti, A., & Fekete, A. (2024). Volunteered geographic information use in crisis, emergency and disaster management: A scoping review and a web atlas. *Geo-spatial Information Science, 27*(2), 423–454. https://doi.org/10.1080/10095020.2022.2139642

14. Jiang, Y., Guo, B., Zhang, X., Tian, H., Wang, Y., & Cheng, M. (2023). A bibliometric and scientometric review of research on crowdsourcing in smart cities. *IET Smart Cities, 5*(1), 1–18. https://doi.org/10.1049/smc2.12048

15. Rizi, M. H. P., & Hosseini Seno, S. A. (2022). A systematic review of technologies and solutions to improve security and privacy protection of citizens in the smart city. *Internet of Things, 20*, 100584. https://doi.org/10.1016/j.iot.2022.100584

16. Chekol, A. G., & Fufa, M. S. (2022). A survey on next location prediction techniques, applications, and challenges. *Journal on Wireless Communications and Networking, 2022*, 29. https://doi.org/10.1186/s13638-022-02114-6

17. Heidari, A., Jafari Navimipour, N., & Unal, M. (2022). Applications of machine learning/deep learning in smart cities and societies based on the internet of things: A systematic literature review. *Sustainable Cities and Society, 85*, 104089. https://doi.org/10.1016/j.scs.2022.104089

18. Weil, C., Bibri, S. E., Longchamp, R., Golay, F., & Alahi, A. A. (2023). Urban digital twin challenges: A systematic review and perspectives for sustainable smart cities. *Sustainable Cities and Society, 99*, 104862. https://doi.org/10.1016/j.scs.2023.104862

19. Mazzetto, S. (2024). A review of urban digital twins integration, challenges, and future directions in smart city development. *Sustainability, 16*(19), 8337. https://doi.org/10.3390/su16198337

20. van Twist, A., Ruijer, E., & Meijer, A. (2023). Smart cities & citizen discontent: A systematic review of the literature. *Government Information Quarterly, 40*(2), 101799. https://doi.org/10.1016/j.giq.2022.101799