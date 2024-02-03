---
title: "Secure Multi-Party Computation for predicting healthcare costs"
draft: false
---

```latex
\documentclass{article}

% Language setting
% Replace `english' with e.g. `spanish' to change the document language
\usepackage[english]{babel}

% Set page size and margins
% Replace `letterpaper' with `a4paper' for UK/EU standard size
\usepackage[letterpaper,top=2cm,bottom=2cm,left=3cm,right=3cm,marginparwidth=1.75cm]{geometry}

% Useful packages
\usepackage{amsmath}
\usepackage{graphicx}
\usepackage[colorlinks=true, allcolors=blue]{hyperref}

\title{Using Secure Multiparty Computing to predict cost of healthcare clinic visits}
\author{Abhinav Srivastava}

\begin{document}
\maketitle

\begin{abstract}
Secure Multiparty Computing (SMC) offers a privacy-preserving method for predicting healthcare clinic visit costs. Utilizing SMC, sensitive patient data is processed across multiple parties without revealing individual inputs, ensuring confidentiality. This approach facilitates accurate cost predictions while adhering to privacy regulations, thus enhancing healthcare planning and resource allocation.
\end{abstract}

\section{Introduction}
In the contemporary realm of healthcare data analytics, Secure Multiparty Computing (SMC) emerges as a pivotal technology for safeguarding patient privacy while enabling accurate cost prediction for clinic visits. This paper introduces a novel framework utilizing SMC, specifically employing the Jiff-MPC JavaScript library in an offline setting. Our approach meticulously processes sensitive patient data across disparate entities without disclosing individual details, thereby upholding stringent confidentiality standards. By integrating diverse data points such as patient demographics, visit types, medical history, and local healthcare economics, we harness the robustness of Random Forest Regression within the SMC paradigm. This methodology not only aligns with privacy regulations but also significantly improves the precision of healthcare cost predictions, thereby informing efficient resource allocation and healthcare management.

\section{Literature Review}
\subsection{Multiparty Computing for Patient Risk Stratification}
In the field of healthcare data analysis, A proposal by Dong, Rudoplh et al., as detailed in their paper \cite{dong2021developing}, marks a significant advancement in secure multi-party computation (MPC) protocols. Their research emphasizes the development of Yao’s garbled circuits and private set intersection techniques, focusing on patient risk stratification. This approach enables the secure linking of patient records and the calculation of critical health metrics without the need for a third-party intermediary. The protocols were rigorously tested on large, synthesized datasets, showcasing their potential for real-world healthcare analytics applications, especially in enhancing inter-institutional data collaboration while maintaining privacy and security.


\subsection{Uses of secure multiparty computing in bioinformatics and adjacent fields}


\subsection{Methodologies}




\bibliographystyle{alpha}
\bibliography{sample}

\end{document}
```