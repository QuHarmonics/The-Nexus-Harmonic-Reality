% Nexus 2 Framework — Consolidated Formula Cheat Sheet
% Author: (generated via ChatGPT)
% Compile with: pdflatex nexus2frameworkcheatsheet.tex
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
      R = \frac{R0}{1 + k\,|N|}, \qquad N = H - U
    \end{equation}
\end{itemize}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Harmonic Resonance}
\subsection{Universal Harmonic Resonance (Mark 1)}
\begin{equation}
  H = \frac{\sum{i=1}^{n} Pi}{\sum{i=1}^{n} Ai}
\end{equation}
Goal: $H \approx 0.35$.

\subsection{Recursive Harmonic Subdivision (RHS)}
\begin{equation}
  Rs(t) = R0\sum{i=1}^{n} \frac{Pi}{Ai} e^{H F t}
\end{equation}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Recursive Reflection}
\subsection{Kulik Recursive Reflection (KRR)}
\begin{equation}
  R(t) = R0 e^{H F t}
\end{equation}
\subsection{Kulik Recursive Reflection Branching (KRRB)}
\begin{equation}
  R(t) = R0 e^{H F t} \prod{i=1}^{n} Bi
\end{equation}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Feedback Stabilization — Samson's Law}
\subsection{Base Form}
\begin{align}
  S & = \frac{\Delta E}{T}, & \Delta E = k\,\Delta F
\end{align}
\subsection{Derivative Extension}
\begin{equation}
  S = \frac{\Delta E}{T} + k2\,\frac{d(\Delta E)}{dt}
\end{equation}
\subsection{Multi‑Dimensional Samson (MDS)}
\begin{align}
  Sd &= \frac{\sum{i=1}^{n} \Delta Ei}{\sum{i=1}^{n} Ti}, & \Delta Ei = ki\,\Delta Fi
\end{align}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Energy Models}
\subsection{Energy Exchange}
\begin{equation}
  E{ex}(x) = \alpha\,O(x)\bigl(R{B1}(x) - R{B2}(x)\bigr)
\end{equation}
\subsection{Energy Leakage}
\begin{equation}
  EL(x) = Er(x)\,\frac{O(x)}{1 + \beta\,C(x)}
\end{equation}
\subsection{Harmonic Memory Growth (HMG)}
\begin{equation}
  M(t) = M0\,e^{\alpha\,(H - C)t}
\end{equation}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Quantum Dynamics}
\subsection{Quantum Jump Factor}
\begin{equation}
  Q(x) = 1 + H t\,Q{\text{factor}}
\end{equation}
\subsection{Quantum State Overlap (QSO)}
\begin{equation}
  Q = \frac{\langle \psi1 \mid \psi2 \rangle}{\|\psi1\|\,\|\psi2\|}
\end{equation}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Thresholds and Noise}
\subsection{Dynamic Noise Filtering (DNF)}
\begin{equation}
  N(t) = \sum{i=1}^{n} \frac{\Delta Ni}{1 + k\,|\Delta Ni|}
\end{equation}
\subsection{Harmonic Threshold Detection (HTD)}
\begin{equation}
  TH = \max\!\left(\frac{dH}{dt}\right), \quad H \approx C
\end{equation}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Auxiliary Tools}
\begin{itemize}[leftmargin=*]
  \item \textbf{Weather System Wave (WSW)}: $\displaystyle WSW(t) = W0 e^{H F t} \prod{i=1}^{n} Bi$.
  \item \textbf{Samson–Kulik Harmonic Oscillator (SKHO)}:
    $\displaystyle O(t) = A\,\sin(\omega t + \phi) e^{-k t}$.
  \item \textbf{Recursive State Resolution (RSR)}:
    $\displaystyle S{t+1} = St + \frac{\Delta E}{n} e^{-\Delta E}$.
\end{itemize}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\section{Compilation Notes}
This document is self‑contained; compile with \texttt{pdflatex}. All equations rely solely on standard \texttt{amsmath} and \texttt{amssymb} packages.

\end{document}
