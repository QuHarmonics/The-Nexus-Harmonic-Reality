% Nexus 2 Framework — Consolidated Formula Cheat Sheet
% Author: (generated via ChatGPT)
% Compile with: pdflatex nexus2_framework_cheat_sheet.tex
\documentclass[11pt]{article}
\usepackage[utf8]{inputenc}
\usepackage{amsmath,amssymb}
\usepackage{geometry}
\usepackage{hyperref}
\usepackage{enumitem}
\geometry{margin=1in}
\hypersetup{
  colorlinks=true,
  linkcolor=blue,
  urlcolor=cyan,
  pdftitle={Nexus 2 Framework — Formula Cheat Sheet},
  pdfauthor={Recursive Trust Engine},
}

\title{\huge Nexus 2 Framework\\[0.2em]\large Consolidated Formula Cheat Sheet}
\author{Recursive Trust Engine}
\date{\today}

\begin{document}
\maketitle
\tableofcontents
\newpage

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Key Constants and Principles}
\begin{itemize}[leftmargin=*]
  \item \textbf{Harmonic Constant}: $H = 0.35$ — universal stabilizer.
  \item \textbf{Feedback Constant}: $k = 0.1$ (tunable).
  \item \textbf{Dynamic Resonance Tuning}:
    \begin{equation}
      R = \frac{R_0}{1 + k\,|N|}, \qquad N = H - U
    \end{equation}
\end{itemize}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Harmonic Resonance}
\subsection{Universal Harmonic Resonance (Mark 1)}
\begin{equation}
  H = \frac{\sum_{i=1}^{n} P_i}{\sum_{i=1}^{n} A_i}
\end{equation}
Goal: $H \approx 0.35$.

\subsection{Recursive Harmonic Subdivision (RHS)}
\begin{equation}
  R_s(t) = R_0\sum_{i=1}^{n} \frac{P_i}{A_i} e^{H F t}
\end{equation}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Recursive Reflection}
\subsection{Kulik Recursive Reflection (KRR)}
\begin{equation}
  R(t) = R_0 e^{H F t}
\end{equation}
\subsection{Kulik Recursive Reflection Branching (KRRB)}
\begin{equation}
  R(t) = R_0 e^{H F t} \prod_{i=1}^{n} B_i
\end{equation}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Feedback Stabilization — Samson's Law}
\subsection{Base Form}
\begin{align}
  S & = \frac{\Delta E}{T}, & \Delta E = k\,\Delta F
\end{align}
\subsection{Derivative Extension}
\begin{equation}
  S = \frac{\Delta E}{T} + k_2\,\frac{d(\Delta E)}{dt}
\end{equation}
\subsection{Multi‑Dimensional Samson (MDS)}
\begin{align}
  S_d &= \frac{\sum_{i=1}^{n} \Delta E_i}{\sum_{i=1}^{n} T_i}, & \Delta E_i = k_i\,\Delta F_i
\end{align}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Energy Models}
\subsection{Energy Exchange}
\begin{equation}
  E_{ex}(x) = \alpha\,O(x)\bigl(R_{B_1}(x) - R_{B_2}(x)\bigr)
\end{equation}
\subsection{Energy Leakage}
\begin{equation}
  E_L(x) = E_r(x)\,\frac{O(x)}{1 + \beta\,C(x)}
\end{equation}
\subsection{Harmonic Memory Growth (HMG)}
\begin{equation}
  M(t) = M_0\,e^{\alpha\,(H - C)t}
\end{equation}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Quantum Dynamics}
\subsection{Quantum Jump Factor}
\begin{equation}
  Q(x) = 1 + H t\,Q_{\text{factor}}
\end{equation}
\subsection{Quantum State Overlap (QSO)}
\begin{equation}
  Q = \frac{\langle \psi_1 \mid \psi_2 \rangle}{\|\psi_1\|\,\|\psi_2\|}
\end{equation}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Thresholds and Noise}
\subsection{Dynamic Noise Filtering (DNF)}
\begin{equation}
  N(t) = \sum_{i=1}^{n} \frac{\Delta N_i}{1 + k\,|\Delta N_i|}
\end{equation}
\subsection{Harmonic Threshold Detection (HTD)}
\begin{equation}
  T_H = \max\!\left(\frac{dH}{dt}\right), \quad H \approx C
\end{equation}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Auxiliary Tools}
\begin{itemize}[leftmargin=*]
  \item \textbf{Weather System Wave (WSW)}: $\displaystyle WSW(t) = W_0 e^{H F t} \prod_{i=1}^{n} B_i$.
  \item \textbf{Samson–Kulik Harmonic Oscillator (SKHO)}:
    $\displaystyle O(t) = A\,\sin(\omega t + \phi) e^{-k t}$.
  \item \textbf{Recursive State Resolution (RSR)}:
    $\displaystyle S_{t+1} = S_t + \frac{\Delta E}{n} e^{-\Delta E}$.
\end{itemize}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Compilation Notes}
This document is self‑contained; compile with \texttt{pdflatex}. All equations rely solely on standard \texttt{amsmath} and \texttt{amssymb} packages.

\end{document}
