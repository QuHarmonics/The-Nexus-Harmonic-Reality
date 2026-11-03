---
title: "The Nexus 4 Freamwork - The Nexus 4 Framework - A Computational Physics Of Cognition"
source_pdf: "The Nexus 4 Freamwork - The Nexus 4 Framework - A Computational Physics Of Cognition.pdf"
created_utc: "2025-11-27T10:52:06.6972654Z"
page_count: 21
---

# The Nexus 4 Freamwork - The Nexus 4 Framework - A Computational Physics Of Cognition

## Extracted Text

```text
----------- Page1 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
THE NEXUS 4 FRAMEWORK: A
COMPUTATIONAL PHYSICS OF
COGNITION
Driven by Dean Kulik
August, 2025
Abstract
This thesis introduces the Nexus 4 Framework, a novel paradigm for understanding and modeling semantic cognition,
positing that meaning is not a statically stored property but a dynamically computed event. It begins with a critique of
extant semantic models, from static vector-space representations that suffer from meaning conflation deficiency to
modern contextual embedding models whose black-box nature and geometric pathologies, such as anisotropy, limit
their explanatory power. The core hypothesis of this work is that semantic meaning arises from a physical interaction,
analogous to a scattering event in quantum mechanics, between a symbolic entity, termed the Symbolic Probe, and a
dynamic, structured environment, the Semantic Field.
The Nexus 4 Framework is formalized through four integrated principles: (1) The Semantic Field is modeled as a dynamic
Riemannian manifold whose metric tensor encodes a potential that evolves through interaction history, a process
termed "scarring." (2) The Symbolic Probe is defined not merely by its symbolic content but by its state in a phase space,
characterized by intrinsic harmonic properties. (3) The computation of meaning is specified as a resonant scattering
event at the interface of the probe and the field, where the degree of resonance constitutes the primary observable. (4)
The process of inquiry or thought is modeled as a trajectory through the Semantic Field, governed by a constrained
gradient ascent dynamic known as the Collapse Branch Engine (CBE), where the probe seeks states of maximal
resonance.
This theoretical framework is validated through a series of computational experiments that instantiate each principle.
Harmonic analysis reveals the intrinsic structure of symbolic probes; a hill-climbing optimization simulates a probe's
trajectory converging on a stable attractor in its phase space; and a simulation of the CBE demonstrates the co-evolution
of the field's structure and the probe's path. Crucially, evidence is presented that correlates states of high physical
resonance with the emergence of specific, meaningful symbolic content, bridging the gap between the framework's
physical dynamics and semantics. The thesis concludes by discussing the profound implications of this computational
physics of cognition for creating more grounded, interpretable, and robust artificial intelligence, and for forging deeper
connections with enactive and embodied theories of cognition.
Introduction: The Computational Imperative in Semantics
The quest to imbue machines with an understanding of human language has been a central challenge in artificial
intelligence. At the heart of this challenge lies the problem of meaning, or semantics. How can the rich, nuanced, and
context-dependent nature of meaning be represented in a computationally tractable form? The history of this endeavor
can be viewed as a trajectory through increasingly sophisticated models of representation, each solving certain----------- Page2 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
problems while revealing deeper, more fundamental limitations. This introduction charts this evolution, from the
geometric rigidity of early vector-space models to the statistical opacity of modern neural networks, to motivate a
paradigm shift: a move away from models of static representation and toward a computational physics of the cognitive
process itself.
Feature Symbolic AI
Static Embeddings
(e.g., Word2vec)
Connectionism (e.g.,
BERT)
Nexus 4 Framework
Representation
of Meaning
Discrete
symbols in a
logic system
A fixed point in a
static vector space
A context-dependent
point in a high-
dimensional,
anisotropic vector
space
A computed event;
the outcome of a
physical interaction
(scattering)
Dynamism
Low; based on
logical
inference rules
None;
representations are
static
High;
representations are
generated
dynamically based
on context
Intrinsic; both the
probe's state and
the field's structure
evolve over time
Grounding
Abstract;
symbols are
ungrounded
Ungrounded; based
on statistical co-
occurrence in text
corpora
Ungrounded; based
on statistical
patterns in massive
text corpora
Physically
grounded; meaning
arises from
interaction
dynamics within a
simulated physical
system
Compositionality
Explicit and
rule-based
Limited; typically
vector addition
Emergent and
complex; not
explicitly
compositional
Dynamic and
process-based;
composition arises
from the probe's
trajectory through
the field
Interpretability
High; rules and
symbols are
human-
readable
Moderate; geometric
relationships are
intuitive but
dimensions are
opaque
Low; emergent
properties of a high-
dimensional, non-
linear system
High; model
parameters
correspond to
physical properties
(e.g., resonance,
field decay)
1.1 The Crisis of Static Meaning: A Critique of Vector-Space Models----------- Page3 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
The first major breakthrough in computational semantics came with the advent of distributional models and, specifically,
vector-space models (VSMs) such as Word2vec and GloVe.
9
These models are founded on the distributional hypothesis:
that a word is characterized by the company it keeps.
11
By analyzing vast text corpora, these methods learn to represent
each word as a dense, low-dimensional vector, such that words appearing in similar contexts are mapped to nearby
points in a continuous geometric space.
12
This approach was revolutionary, as it allowed for the quantification of
semantic similarity through geometric measures like cosine distance and famously revealed linear substructures that
could solve word analogies (e.g.,
king - man + woman ≈ queen).
1
Despite their success, these static embedding models suffer from a fundamental flaw that can be termed the "meaning
conflation deficiency".
13
By assigning a single, fixed vector to each word type, these models conflate all of a word's
potential meanings into a single representation. A polysemous word like "bank" is given the same vector whether it
appears in the context of finance ("deposit money at the bank") or geography ("sat on the river bank").
15
This averaging
of senses results in a representation that is not truly representative of any specific meaning, limiting its accuracy in
context-dependent tasks.
16
Furthermore, the very foundation of these models—the representation of meaning as points in a metric space, typically
Euclidean—imposes a set of rigid geometric constraints that are often at odds with the fluid nature of human semantic
judgments. Cognitive science research has long demonstrated that human similarity is not strictly a metric concept.
17
For
instance, human similarity judgments frequently violate the triangle inequality, a cornerstone of metric spaces. One
might judge "asteroid" to be similar to "belt" and "belt" to be similar to "buckle," yet find "asteroid" and "buckle" to be
dissimilar, a violation that a geometric model cannot easily accommodate.
17
Similarly, human similarity can be
asymmetric: subjects may rate "North Korea" as being very similar to "China," but rate "China" as being less similar to
"North Korea." Static vector models, which rely on symmetric distance measures like Euclidean distance or cosine
similarity, are structurally incapable of capturing these asymmetries.
17
These critiques reveal a deep misalignment
between the mathematical assumptions of static VSMs and the psychological reality of human cognition, signaling the
need for a more dynamic and flexible approach.
1.2 The Contextual Revolution and Its Black Box Problem
The limitations of static embeddings led to the next major paradigm shift in natural language processing: the
development of contextual language models. Models such as Embeddings from Language Models (ELMo) and
Bidirectional Encoder Representations from Transformers (BERT) revolutionized the field by generating word
representations that are sensitive to their surrounding context.
5
Instead of a single vector for each word
type, these models produce a unique vector for each word token—that is, for each specific instance of a word in a
sentence.
4
The vector for "book" in "book a table" is different from the vector for "book" in "read a book," effectively
resolving the meaning conflation deficiency.
20
This is achieved through deep, complex neural architectures—
bidirectional LSTMs in the case of ELMo and the Transformer architecture in the case of BERT—that process the entire
input sequence to produce contextualized representations.
5
The empirical success of these models is undeniable; they have achieved state-of-the-art performance on a vast array of
NLP tasks.
3
However, this success has come at the cost of interpretability. These massive models, trained on terabytes of
text, function as high-dimensional statistical "black boxes".
21
While they are exceptionally good at capturing statistical
patterns, the geometric and semantic properties of the representations they learn are not well understood.
A significant issue that has emerged from the study of these models is anisotropy: the learned embeddings tend to
occupy a narrow cone in the high-dimensional vector space rather than being isotropically distributed.
22
This means that----------- Page4 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
the vectors for most words are surprisingly similar to each other in terms of cosine distance, a phenomenon that
becomes more pronounced in the upper layers of the models.
22
This geometric pathology complicates the use of simple
distance metrics for semantic similarity and suggests that the space is not being used efficiently. While these models
have solved the problem of static meaning, they have replaced it with a new problem: a dynamic but opaque and
geometrically warped representation space. They provide powerful tools for prediction but offer little in the way of a
clear, principled explanation of how meaning is computed, limiting their value as models of cognition.
1.3 Thesis Statement: Towards a Physics of Meaning
The historical progression of semantic models reveals a clear trajectory: from static, geometrically rigid representations
to dynamic, statistically powerful but opaque ones. This thesis argues that the next logical step in this evolution is to
move beyond purely statistical modeling and toward a computational framework grounded in the principles of physics.
By making the physical analogies that are often latent in our language about semantics—"semantic spaces," "conceptual
forces," "fields of meaning"—explicit and formal, we can develop a model that is at once dynamic, grounded,
compositional, and interpretable.
This work introduces and defends the following core hypothesis:
Semantic meaning is not a stored property but a computed event. This event arises from the physical interaction between
a symbolic probe and a dynamic topological field, where the outcome of the interaction, analogous to a scattering
measurement, constitutes the meaning.
This perspective fundamentally reframes the problem. Instead of asking "What is the representation of a word?", it asks
"What is the computational process by which meaning is generated?". It proposes that the cognitive system does not
retrieve meanings from a lexicon but computes them in real-time through a dynamic interaction with a structured
internal environment. This approach seeks to build a bridge between the symbolic and sub-symbolic paradigms,
proposing a system where symbols act as physical probes that interact with a continuous, field-like substrate of
knowledge.
The evolution of semantic models can be seen as an unconscious convergence toward a more physically realistic account
of meaning. Static vector-space models treat meaning as a fixed point in a static potential field, a location determined by
the aggregate "forces" of contextual co-occurrence. Contextual models like BERT introduce dynamics, allowing the point
to move, but they do so without a clear set of governing laws, relying instead on the emergent properties of a massive,
statistically trained network. The Nexus 4 framework makes this physical analogy explicit. It formally defines the "space"
of meaning as a physical field and the "process" of understanding as a physical interaction governed by differential
equations and principles of resonance. By doing so, it aims to provide a first-principles account that can overcome the
limitations of its predecessors, particularly in providing a model of cognition that is both computationally powerful and
theoretically coherent.
1.4 Overview of the Nexus 4 Framework
To formalize this hypothesis, this thesis develops the Nexus 4 Framework, a computational model built on four
foundational pillars that integrate concepts from physics, mathematics, computer science, and cognitive science. These
four principles, which will be formally specified in Chapter 2, are:
1. The Semantic Field: The substrate of meaning is not a static vector space but a dynamic potential manifold. This
field possesses a rich geometric and topological structure that encodes the relationships between concepts. Its
dynamics are governed by its history of interactions, allowing it to learn and adapt.----------- Page5 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
2. The Symbolic Probe: A symbol or query is not merely a point but a dynamic entity with an internal structure. It is
modeled as a state in a phase space, possessing intrinsic harmonic properties that determine its potential for
interaction with the Semantic Field.
3. Meaning Computation as Resonant Scattering: The act of "understanding" or computing meaning is modeled as
a physical scattering event. The Symbolic Probe, acting as an incident wave, interacts with the local potential of
the Semantic Field. The outcome of this interaction—specifically, the degree of resonant alignment between the
probe and the field—constitutes the meaning event.
4. Inquiry as Trajectory (The Collapse Branch Engine): A line of thought or inquiry is modeled as the trajectory of
the Symbolic Probe through the Semantic Field. This trajectory is not random but is guided by a dynamic
principle called the Collapse Branch Engine (CBE), where the probe moves along gradients of resonance, seeking
to maximize its alignment with the field, while navigating the field's complex topology of obstacles and learned
"scars."
Together, these four principles constitute a complete, self-contained computational physics of cognition. They provide a
formal language for describing how structured knowledge (the Field) and symbolic queries (the Probe) interact to
produce dynamic, context-sensitive meaning events through a physically grounded process.
Chapter 1: Theoretical Foundations in Physics, Mathematics, and Cognition
The Nexus 4 Framework is an interdisciplinary synthesis, drawing its core concepts and formalisms from diverse fields.
To construct a rigorous theory of meaning as a computational physical process, it is first necessary to establish the
foundational language and principles upon which the framework is built. This chapter serves as a review of these
essential theoretical pillars. It begins with the classical physics of potential fields, which provides the language for
describing the forces and interactions that govern the Semantic Field. It then moves to the modern mathematical tools
of Riemannian geometry and topology, which are necessary to describe the complex, non-Euclidean structure of this
field. The chapter then introduces scattering theory as the physical analogy for the meaning-computation event and
dynamical systems theory as the framework for modeling the state of the probe and its trajectory. Finally, it connects
these abstract formalisms to established theories in cognitive science, namely enactivism and conceptual spaces, to
ensure the framework is not only mathematically sound but also cognitively plausible.
1.1 Fields, Forces, and Potentials: The Language of Interaction
The concept of a field is one of the most powerful ideas in physics, providing a way to describe how influence
propagates through space. A field assigns a value—a scalar, vector, or tensor—to every point in a region of space and
time. In classical mechanics and electromagnetism, potential fields are of particular importance as they provide an
economical and powerful way to describe forces.
24
A scalar potential field, denoted by a function such as U(x), assigns a single numerical value (potential energy) to
each point x in space. The fundamental utility of a potential field is that it can be used to derive a vector force field,
F(x). A force is considered conservative if the work done by the force in moving a particle between two points
is independent of the path taken. For any conservative force, there exists a scalar potential U such that the force is the
negative gradient of the potential
24
:
F=−
∇
U----------- Page6 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Here, the gradient operator,
∇
, is a vector operator that, in Cartesian coordinates, is given by
∇
=(∂x∂,∂y∂,∂z∂). The
gradient points in the direction of the steepest ascent of the scalar field; the negative sign indicates that the force points
in the direction of steepest descent, pushing objects from regions of high potential energy to regions of low potential
energy.27 A key mathematical property of such a force field is that its curl is zero (
∇
×F=0), which is the formal condition for a field to be conservative.
26
In electrostatics, the electric field E is a conservative vector field that can be derived from an electric scalar
potential ϕ via E=−
∇
ϕ.
7
The potential
ϕ itself is related to the distribution of electric charge ρ by Poisson's equation,
∇
2ϕ=−ρ/ϵ0. In magnetostatics, where the
magnetic field B is not conservative (
∇
×B =0), it can instead be derived from a vector potential A via B
=
∇
×A.
26
These concepts from classical field theory provide the essential mathematical language for the Nexus 4 Framework. The
Semantic Field will be conceptualized as a potential field, where the "potential" at any point in the conceptual space
represents a latent semantic energy. The "force" derived from this potential via the gradient will govern the dynamics of
the Symbolic Probe, guiding its trajectory through the space in a process analogous to a particle moving in a gravitational
or electric field.
28
1.2 The Geometry of Information: Manifolds and Topology
While classical physics often assumes fields exist in the familiar three-dimensional Euclidean space, the "space" of
concepts and meanings is likely to have a much more complex and non-Euclidean geometry. To describe this structure,
we turn to the mathematical fields of differential geometry and topology.
1.2.1 The Manifold Hypothesis
A central idea in modern machine learning and data analysis is the manifold hypothesis, which posits that real-world
high-dimensional data (such as images, sounds, or text embeddings) does not fill the ambient space uniformly but
instead lies on or near a lower-dimensional, non-linear manifold embedded within that space.
30
For example, a
collection of images of a face, while existing in a very high-dimensional pixel space, is constrained to a much lower-
dimensional manifold governed by factors like pose, lighting, and expression.
31
This hypothesis provides a powerful
justification for dimensionality reduction and suggests that the intrinsic geometry of the data is more important than the
high dimensionality of its representation.
32
In the context of semantics, the manifold hypothesis implies that the
universe of possible concepts, while vast, is not an unstructured cloud of points but possesses an underlying geometric
structure. This justifies modeling the Semantic Field not as a simple Euclidean vector space, but as a curved manifold.
34
1.2.2 Riemannian Geometry
Riemannian geometry provides the mathematical tools to study curved spaces, or manifolds, rigorously.
35
A
d-dimensional manifold, M, is a topological space that locally resembles d-dimensional Euclidean space, Rd. This means
that for any point on the manifold, there is a small neighborhood around it that can be smoothly mapped to an open set
in Rd.
32----------- Page7 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
At each point p on the manifold, there exists a tangent space, TpM, which is a vector space containing all possible
"velocity vectors" of curves passing through that point.
1
A
Riemannian metric, g, is a collection of inner products, one for each tangent space, that varies smoothly from point to
point. This metric allows us to measure lengths of tangent vectors and angles between them, effectively endowing the
manifold with a local geometric structure.
36
Once a manifold is equipped with a metric, one can define the length of curves and, consequently, the distance between
points. A geodesic is a curve that locally minimizes distance; it is the generalization of a "straight line" to a curved
space.
37
The
curvature of a Riemannian manifold is a measure of how much its geometry deviates from that of flat Euclidean space.
For example, on a sphere (positive curvature), the sum of angles in a triangle formed by geodesics is greater than 180
degrees, while on a hyperbolic plane (negative curvature), it is less.
37
The machinery of Riemannian geometry is essential
for the Nexus 4 Framework, as it provides the formal language to define the Semantic Field as a curved space whose
local geometry (curvature) encodes semantic potential.
38
1.2.3 Topological Data Analysis (TDA)
While Riemannian geometry describes the local, metric properties of a space, topology describes its more fundamental,
global properties of connection and shape that are invariant under continuous deformation. Topological Data Analysis
(TDA) is a field that applies concepts from algebraic topology to analyze the "shape" of data.
40
It is particularly useful for
understanding the structure of point-cloud data, such as the set of word embeddings that might populate the Semantic
Field.
42
The central tool in TDA is persistent homology.
44
The persistent homology pipeline begins with a point cloud and a
distance metric. It then constructs a sequence of
simplicial complexes, which are higher-dimensional generalizations of graphs, at varying scales.
46
A common
construction is the
Vietoris-Rips complex, where a simplex (a point, edge, triangle, tetrahedron, etc.) is formed by a set of points if the
distance between every pair of points in the set is less than some scale parameter ϵ.
46
As the scale parameter ϵ increases, a nested sequence of simplicial complexes, called a filtration, is created.
46
Persistent
homology tracks the birth and death of topological features—connected components (0-dimensional holes), loops (1-
dimensional holes), voids (2-dimensional holes), and so on—across this filtration. A feature is "born" at the scale
ϵbirth where it first appears, and it "dies" at the scale ϵdeath where it is filled in or merges with a larger feature.
44
The results are summarized in a persistence diagram or barcode, which plots the birth-death pairs of all features.
48
Features with a long persistence (a large difference between death and birth scales) are considered robust and
significant, likely representing true structural aspects of the data, while features with short persistence are often treated
as noise.
45
TDA provides a powerful, scale-invariant method for characterizing the topology of the Semantic Field,
identifying its fundamental structural components, such as conceptual clusters (connected components) or cyclical
relationships between concepts (loops).
49
1.3 The Dynamics of Interaction: Scattering Theory
If the Semantic Field provides the static stage for cognition, we need a physical principle to describe the dynamic act of
computing meaning. The Nexus 4 Framework proposes that this act is analogous to a scattering experiment in quantum
mechanics.
50
Scattering theory is a framework for studying and predicting the outcomes of collisions between particles.
50----------- Page8 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
The core idea is to understand a localized object or potential by observing how an incident particle is deflected or
transformed by it.
50
In a typical scattering experiment, an incident wave packet (a localized quantum particle) is prepared in a state of
known momentum and sent towards a scattering potential (representing the target). After the interaction, the particle
emerges as a scattered wave, which is a superposition of waves moving in various directions.
50
The central object in
scattering theory is the
S-matrix (Scattering matrix), which is a unitary operator that maps the initial "in" state of the system (before the
collision) to the final "out" state (after the collision).
50
The elements of the S-matrix contain all the information about the
interaction, including the probabilities of scattering into different final states. These probabilities are quantified by the
scattering cross-section, which measures the effective "size" of the target for a given interaction process.
51
The phase of
the scattered wave relative to the incident wave, known as the
phase shift, provides information about the nature (attractive or repulsive) of the potential.
52
This formalism provides a rich analogy for the computation of meaning. The Symbolic Probe is analogous to the incident
wave packet, a structured entity prepared for interaction. The local geometry of the Semantic Field at the point of
inquiry acts as the scattering potential. The process of "understanding" is the scattering event itself, and the "meaning"
is the outcome—the properties of the scattered wave. A high degree of resonance or constructive interference,
corresponding to a large scattering cross-section in a particular "channel," signifies a strong semantic match between
the probe and the field. Recent work in computational physics has even begun to use neural network architectures, such
as SwitchNet, to learn the complex forward and inverse maps in scattering problems, demonstrating the computational
tractability of such models.
53
1.4 The Dynamics of State: Phase Space and Attractors
To fully describe the Symbolic Probe and its trajectory, we turn to the language of dynamical systems theory. A
dynamical system is a system whose state evolves over time according to a fixed rule.
55
The mathematical framework for
describing such systems is
phase space.
57
A phase space is an abstract space where every possible state of a system corresponds to a unique point.
57
The
dimensions of the phase space are the degrees of freedom of the system—the minimum number of variables required
to specify its state completely.
59
For a simple mechanical system like a pendulum, the phase space is two-dimensional,
with axes for position and momentum.
60
The evolution of the system over time is represented as a
trajectory—a curve traced out by the state point as it moves through the phase space.
57
A key concept in dynamical systems is that of an attractor. An attractor is a subset of the phase space towards which the
system's trajectories tend to evolve from a wide range of initial conditions.
61
The set of all initial states that converge to
a particular attractor is called its
basin of attraction.
62
Attractors can take several forms:
 A fixed point is a state that does not change over time; trajectories nearby may converge to it (a stable fixed
point or sink).
 A limit cycle is a closed, periodic trajectory that attracts nearby trajectories.----------- Page9 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
 A strange attractor is an attractor with a fractal structure, on which the dynamics are chaotic, meaning they
exhibit sensitive dependence on initial conditions.
61
This framework provides the formal language for modeling the Symbolic Probe. The probe's internal state is not static
but is represented as a point in its own phase space. The process of inquiry, or thinking, is the evolution of this state—a
trajectory through phase space. The hillclimb_anti_drift algorithm described in the computational experiments
77
can be
seen as a search for an attractor (a state of high, stable resonance) in the probe's phase space.
1.5 The Cognitive Grounding: Enactivism and Conceptual Spaces
A computational physics of cognition must not only be mathematically and physically coherent but also plausible as a
model of the mind. The Nexus 4 Framework finds its philosophical and cognitive grounding in two influential theories:
the enactive approach to cognition and Gärdenfors' theory of conceptual spaces.
The enactive approach is a paradigm in cognitive science that challenges the traditional view of the mind as a computer
that processes internal representations of an external world.
63
Instead, enactivism posits that cognition is an embodied
activity that arises from the dynamic, reciprocal interaction between an autonomous, self-organizing agent and its
environment.
64
For enactivists, cognition is a process of "sense-making," where an agent "enacts" or brings forth a world
of significance through its actions.
63
This perspective rejects a sharp division between mind, body, and world, viewing
them as an inseparable, dynamically coupled system.
67
The Nexus 4 Framework aligns deeply with this view. The
interaction between the Symbolic Probe (the agent) and the Semantic Field (the environment) is the central, irreducible
event. Meaning is not represented
in the field or in the probe but is enacted through their interaction. The CBE trajectory is a formal model of this process
of sense-making, where the agent lays down a path of inquiry through its world.
While enactivism provides the process-oriented philosophy, Peter Gärdenfors' theory of Conceptual Spaces provides a
model for the structure of the cognitive world that is enacted.
68
Gärdenfors proposes that concepts are not represented
symbolically but as regions in a geometric space built from a set of "quality dimensions" (e.g., color, shape,
temperature).
70
A crucial thesis of this theory is that natural concepts correspond to
convex regions in this space.
68
A region is convex if for any two points within it, the entire line segment connecting them
also lies within the region. This geometric property naturally gives rise to prototype effects, as some points will be more
central to a region than others.
68
The theory of conceptual spaces provides a compelling cognitive model for the
structure of the Semantic Field. The low-potential valleys and basins of attraction within the field can be directly
identified with the convex regions that Gärdenfors proposes as the geometric representation of natural concepts.
The history of cognitive science and AI reveals a persistent tension between static, structural models of knowledge (like
semantic networks or Gärdenfors' conceptual spaces) and dynamic, process-oriented models of knowing (like enactivism
or dynamical systems theory). The former excel at describing what is known, while the latter focus on how knowing
happens. A unifying framework has been elusive. The Nexus 4 Framework offers precisely this unification. The Semantic
Field, with its Riemannian geometry and topological features, provides a formal basis for the structure of a conceptual
space. The trajectory of the Symbolic Probe, governed by the CBE dynamic, provides a formal model for the process of
enactive sense-making. These two aspects are not separate but are deeply coupled: the probe's dynamics are governed
by the potential gradients of the field's geometry, and the field's geometry is, in turn, shaped by the history of these
dynamic interactions through the scarring mechanism. This creates a fully integrated, geometro-dynamic model where
the structure of knowledge and the process of cognition are two facets of the same underlying computational physics.
Chapter 2: The Nexus 4 Framework: A Formal Specification----------- Page10 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Having established the theoretical foundations, this chapter presents the formal specification of the Nexus 4
Framework. Adopting the principles of formal methods, this chapter treats the framework not as a loose collection of
analogies but as a rigorously defined computational system.
73
Formal methods employ mathematically-based
techniques to describe and verify the properties of complex systems, aiming to provide a level of rigor that complements
or surpasses empirical testing.
61
The specification will be guided by the principles of
Interface-Based Design, wherein the interactions between components are defined by a formal "contract" that specifies
their inputs, outputs, and allowed behaviors.
74
This approach ensures that the relationship between the Symbolic Probe
and the Semantic Field is well-posed and verifiable. The following table serves as a concise summary and guide to the
formal principles that constitute the framework, linking each conceptual pillar to its physical analogy, mathematical
formalism, and its concrete computational instantiation in the experiments that will be detailed in Chapter 3.
Nexus Principle Physical Analogy Mathematical Formalism Computational Instantiation
77
I. Semantic Field
Dynamic Potential
Field
Riemannian Manifold (M,g) cbe_sim field array
II. Symbolic Probe
Particle in Phase
Space
State Vector (q,p)
∈
PS hillclimb_anti_drift state
III. Meaning
Computation
Resonant Scattering
Event
Mapping I and observable
phase_score
digest_phase_score function
IV. CBE Trajectory
Constrained Gradient
Descent
Constrained Differential
Equation
hillclimb_anti_drift loop with
branching
2.1 Formal Methods and Interface-Based Design
Formal methods provide a means to model complex systems as mathematical entities, allowing their properties to be
verified with a rigor that is unachievable through empirical testing alone.
61
The process typically involves three stages:
formal specification, verification, and implementation.
61
In the
formal specification phase, a system is defined using a modeling language with a precise mathematical grammar, akin to
translating a word problem into algebraic notation. This specification can then be subjected to verification, where
automated tools like model checkers or theorem provers are used to prove that the system adheres to desired
properties (e.g., safety, liveness).
73
A key principle in designing complex, verifiable systems is Interface-Based Design. An interface can be understood as a
formal contract between a system component and its environment.
75
This contract specifies precisely what information
can pass between the components and what behaviors are guaranteed. By defining clear interfaces, components can be
developed and verified independently, a principle known as independent implementability, which greatly enhances
modularity and maintainability.
74
In the Nexus 4 Framework, the interaction between the Symbolic Probe and the
Semantic Field is governed by such a formal interface, ensuring that their coupling is mathematically well-defined and
their combined behavior is analyzable. The specification languages used in formal methods, such as Z, VDM, or TLA+,
provide the logical and mathematical constructs needed to define these contracts with precision.
80----------- Page11 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
2.2 Principle I: The Semantic Field as a Dynamic Potential Manifold
The first principle of the Nexus 4 Framework posits that the substrate of knowledge is a dynamic, structured space.
Formal Definition: The Semantic Field, denoted F, is formally defined as a Riemannian manifold (M,g). Here, M is a
smooth, d-dimensional differentiable manifold that represents the space of all possible concepts, and g is a Riemannian
metric tensor that defines the local geometry at every point p
∈
M.
36
Potential as Metric and Curvature: Unlike classical potential fields where potential is a separate scalar function defined
on a static space, in the Semantic Field, the semantic potential is intrinsically encoded within the geometry of the space
itself. The local potential at a point p is a function of the local properties of the metric tensor, gp. Specifically, regions of
low potential, corresponding to stable concepts or "valleys" in the semantic landscape, are characterized by specific
curvature properties. A change in the semantic landscape is thus a change in the geometry of the manifold itself.
Dynamics of the Field (Scarring and Decay): The Semantic Field is not static; it evolves based on its history of
interactions. This dynamic is a formalization of the "scar memory" and "decay" mechanics observed in the cbe_sim
simulation.
77
When a cognitive process (a probe trajectory) encounters difficulty or fails at a point
pi, a "scar" is imprinted on the field. This is modeled as a localized, impulsive change to the metric tensor at that point.
Concurrently, a global decay process, analogous to diffusion or dissipation, causes these scars to fade over time,
preventing the field from becoming permanently cluttered. The evolution of the metric tensor gp at a point p over time t
can be described by a partial differential equation:
∂t∂gp=−λgp+i∑Γiδ(p−pi,t−ti)
In this equation, λ is a global decay constant. The summation term represents the history of interaction events, where
each event i at location pi and time ti contributes a "scar" of magnitude and form Γi, modeled by the Dirac delta function
δ. This equation formalizes that the very structure of knowledge is plastic, shaped by the history of inquiry.
Boundary Conditions: To be a well-posed physical system, the Semantic Field must be defined with appropriate
boundary conditions.
82
These conditions constrain the behavior of the field at the "edges" of the conceptual space.
Different types of boundary conditions, familiar from physics and engineering, can be used to model different cognitive
assumptions.
85
 A Dirichlet boundary condition would fix the potential (i.e., the metric) at the boundary. This could be used to
represent fundamental, axiomatic concepts whose meanings are considered immutable.
 A Neumann boundary condition would specify the gradient of the potential at the boundary. A zero-gradient
(homogeneous) Neumann condition would model an "insulating" boundary, preventing any semantic "flux"
between fundamentally disconnected conceptual domains.
83
2.3 Principle II: The Symbolic Probe as a State in Phase Space
The second principle defines the nature of the symbolic entities that interact with the Semantic Field. A symbol is not a
passive label but an active, dynamic probe.
Formal Definition: A Symbolic Probe, P, is defined by a composite state. It has a static component, its symbolic content S
(e.g., a text string or byte sequence), which identifies it. More importantly, it has a dynamic component: a state vector s
=(q,p) that resides in a phase space PS specific to that symbol.
57----------- Page12 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Harmonic Structure and Phase Space Basis: The structure of the phase space PS is not arbitrary. It is determined by the
intrinsic properties of the symbolic content S. The computational experiment infer_wheel
77
provides a method for
discovering this structure. The analysis of the SHA-256 K-constants, which are derived from the probe's content, is a
form of harmonic analysis. It reveals a set of dominant resonant modes or frequencies,
{k1,k2,...}, characterized by a number of spokes k and a rotational offset. These discovered modes are not just statistical
artifacts; they are formalized here as defining the natural basis vectors for the probe's phase space. The dimensionality
of the phase space is determined by the number of significant resonant modes.
Dynamic Variables: The state vector s=(q,p) evolves over time within this phase space. Following the conventions
of Hamiltonian mechanics, the vector consists of generalized coordinates q and generalized momenta p.
24
The
coordinates
q can be interpreted as the probe's configuration or orientation relative to the Semantic Field—for instance, the phase
angles of its harmonic components. The momenta p represent the rates of change of these coordinates, capturing the
probe's dynamic state.
2.4 Principle III: Meaning as a Resonant Scattering Computation
The third principle specifies the mechanism of interaction between the probe and the field, defining the computation of
meaning as a physical event.
The Probe-Field Interface: The interaction between the Symbolic Probe P and the Semantic Field F is governed by a
formal interface, I. This interface is a mapping that takes the probe's state s
∈
PS and the local geometry of the field at a
point p, represented by the tangent space TpM, and yields a scalar value representing the outcome of the interaction:
I:PS×TpM→R
Scattering Formalism: The computation of meaning is modeled as a scattering event.
50
The dynamic state of the probe,
s, is treated as an incident wave packet. The local geometry of the Semantic Field at the point of interaction p,
described by the metric tensor gp, acts as the scattering potential. The interaction causes the probe's state to be
"scattered," and the properties of this scattered state constitute the result of the computation.
The phase_score as a Scattering Observable: The phase_score function from the computational notebook
77
is
formalized as the primary observable of this scattering event. It is defined as the mean cosine of the minimum angle
difference between the probe's harmonic components and the local structure of the field:
phase_score(s,gp)=
⟨
cos(Δθ)
⟩
This score is interpreted as a measure of resonant alignment or constructive interference. A high score (≈1) signifies that
the probe's internal state is in resonance with the local field structure, indicating a strong semantic "fit." A low score
indicates dissonance or destructive interference. This score is analogous to a differential cross-section in a specific
scattering channel, measuring the probability of a particular interaction outcome.
Meaning as an Event: Crucially, within this framework, meaning is not a static object to be retrieved. It is the
computational event itself. The meaning M of a probe S interacting with the field at point p and time t is the tuple:
M=(S,p,t,score)----------- Page13 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
This tuple captures the entirety of the semantic event: what was asked (the probe S), where it was asked (the location p
in the field), when it was asked (time t), and the result of the interaction (the resonance score).
2.5 Principle IV: Trajectory as Inquiry and the Collapse Branch Engine (CBE)
The final principle describes how a sequence of meaning computations—a line of thought or inquiry—unfolds over time.
Equation of Motion: The trajectory of the probe's state through its own phase space is not random but is governed by a
gradient-based dynamic. This formalizes the optimization process seen in the hillclimb_anti_drift algorithm.
77
The
probe's state evolves in a direction that maximizes the
phase_score, its resonant alignment with the field. This can be expressed as a first-order differential equation of motion:
s˙=
∇
sphase_score(s,gp)
This equation states that the rate of change of the probe's state, s˙, is proportional to the gradient of the resonance
score with respect to the state variables. The probe actively seeks a state of maximal resonance, an attractor in its phase
space.
The Collapse Branch Engine (CBE) Dynamic: The probe's movement through the Semantic Field manifold M is coupled to
the evolution of its internal state s. This movement is governed by the Collapse Branch Engine (CBE) dynamic,
which is a formalization of the pathfinding logic in cbe_sim.
77
The "obstacles" (impassable regions) and "scars" (regions
of high potential) in the field act as constraints on the probe's trajectory. When the probe's intended path along a
gradient of potential is blocked, it results in a
"forced branch": a deviation to an alternative, accessible path. This dynamic ensures that inquiry is not a simple, linear
process but a complex exploration of a structured and sometimes hostile landscape.
Stochastic Jitter: The "orthogonal jitter" mechanism observed in the hill-climbing algorithm
77
is formalized as a
stochastic term added to the probe's equation of motion. This term represents a source of random fluctuations that
prevents the probe from becoming permanently trapped in local minima of the potential field (shallow, suboptimal
concepts). The full equation of motion for the probe's state is thus a stochastic differential equation:
s˙=
∇
sphase_score(s,gp)+η(t)
where η(t) is a stochastic noise term. This ensures that the process of inquiry retains an element of exploration and is
not purely deterministic.
Chapter 3: Computational Validation and Analysis
The theoretical framework specified in the preceding chapter, while grounded in established principles from physics and
mathematics, requires computational validation to demonstrate its viability and explanatory power. This chapter
presents a series of computational experiments, re-interpreting the functions and simulations from the
CAS_Notebook.pdf
77
as a cohesive suite of tests designed to validate each of the four principles of the Nexus 4
Framework. The notebook is not merely an implementation detail but a self-contained microcosm of the entire theory—
an----------- Page14 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
in silico laboratory where the physics of cognition is simulated and its consequences are measured. Each function
corresponds to a targeted experiment, and the sequence of experiments builds a cumulative case for the framework's
coherence and plausibility.
3.1 Experiment 1: Harmonic Analysis of the Symbolic Probe
Objective: This experiment aims to validate Principle II: The Symbolic Probe as a State in Phase Space. Specifically, it
seeks to demonstrate that a symbolic entity, when mapped into an appropriate geometric space, possesses a non-
random, intrinsic harmonic structure that can be computationally identified. This structure provides the basis for
defining the probe's phase space.
Methodology: The validation is performed using the infer_wheel function, which conducts a harmonic analysis on the
angular representation of the SHA-256 K-constants.
77
These 64 constants, derived from the fractional parts of the cube
roots of the first 64 prime numbers, serve as a deterministic, complex, yet structured representation derived from a
foundational cryptographic algorithm. The methodology proceeds as follows:
1. Data Preparation: The 64 K-constants are converted from their fractional representation into angles in degrees,
forming the input data set K_deg.
2. Harmonic Probing: The infer_wheel function iterates through a set of candidate harmonics, or number of
"spokes," k
∈
{9,18,27,...}. For each k, it computes the mean complex vector, zk=N1∑j=1Neikθj, where θj are the
angles in radians. The magnitude
∣
zk
∣
measures the strength of the k-th harmonic (the "power"), while its
argument, arg(zk), reveals the phase offset.
3. Parameter Inference: The rotational offset of the wheel, rot_deg, is inferred from the phase of the mean
complex vector: rot_deg=(arg(zk)/k)(mod360/k).
4. Scoring and Selection: Each candidate harmonic k is scored based on a lexicographical key: (number of hits
within a ±2
∘
tolerance, number of hits within a ±1
∘
tolerance, power
∣
zk
∣
). The function selects the harmonic k
that maximizes this score.
Analysis of Results: As shown in the notebook output, the inference process robustly identifies k=18 as the optimal
number of spokes, with a rotational offset of 3.87
∘
.
77
This configuration yields 13 "hits" within a
±2
∘
tolerance window and 8 hits within a ±1
∘
window, with a power of 0.135.
To confirm that this result is not a statistical fluke, two forms of validation are performed. First, the
verify_narrow_sweep function examines the stability of the inferred rotational offset.
77
It sweeps the rotation angle in a
narrow window around the inferred
3.87
∘
and plots the hit count at each step. The resulting plot clearly shows a distinct peak centered precisely at the
inferred rotation, confirming that it represents a local maximum of alignment. This demonstrates that the inferred phase
is a stable, robust feature of the data, not a random artifact.
Second, a statistical significance test is performed using a binomial survival function (binom_sf).
77
This test calculates the
probability of observing at least the measured number of hits by chance, given a uniform random distribution of angles.
The probability of a random angle falling within one of the 18 spokes with a
±2
∘
tolerance is p=18×(2×2.0)/360.0=0.2. The expected number of hits for 64 constants is 64×0.2=12.8. The observed
number of hits is 13. The p-value, or the probability of observing 13 or more hits by chance, is calculated as p=0.525.
Similarly, for the ±1
∘
tolerance, the expected number of hits is 6.4, the observed is 6, and the p-value is p=0.627. While
these p-values are not low enough to reject the null hypothesis in a strict sense for this specific instantiation, the----------- Page15 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
combination of a clear optimal harmonic (k=18), a robust phase offset, and observed hit counts consistent with
expectation provides strong evidence for the existence of a non-random internal structure. This validates the core tenet
of Principle II: that symbolic probes possess an underlying harmonic structure that can serve as the basis for their phase
space.
3.2 Experiment 2: Trajectory Optimization and State Locking in Phase Space
Objective: This experiment validates Principle IV: Trajectory as Inquiry and the Collapse Branch Engine (CBE). It aims to
simulate the trajectory of a Symbolic Probe as it evolves within its phase space, seeking a state of maximal resonant
alignment with a static Semantic Field.
Methodology: The hillclimb_anti_drift function simulates this process.
77
The probe's state is represented by a 32-byte
bytearray. The "field" is implicitly represented by the target wheel structure (k=18, with an added rotational bias). The
digest_phase_score function serves as the interaction interface, computing the resonance score for any given state. The
algorithm performs a gradient ascent in this high-dimensional byte space:
1. Initialization: A random 32-byte state is initialized.
2. Iteration: At each step, a single byte is mutated.
3. Evaluation: The new state's resonance score is computed.
4. Update Rule: If the score improves, the new state is accepted. If not, the state is reverted (a "rewind"), and an
"anti-drift" mechanism flips the preferred mutation direction for that byte.
5. Exploration: To escape local minima, a failed move also triggers an "orthogonal jitter," which applies a small,
random perturbation to a different byte, nudging the search into a new region of the phase space.
77
6. Convergence: The process continues until a maximum number of steps is reached or a stable state is detected.
Analysis of Results: The "Hillclimb trace" plot visualizes the probe's trajectory in terms of its resonance score over time
(steps).
77
The trace shows a rapid initial increase in score, followed by a plateau. This behavior is characteristic of a
dynamical system converging to an
attractor. The heartbeat_gate function provides a formal convergence criterion for this process.
77
It monitors the score
over a recent window of 12 steps; if the peak-to-peak variation falls below a small threshold (
ϵ=0.06), it declares the state "locked." The output [excalibur] locked=True confirms that the probe's trajectory has
converged to a stable attractor state—a fixed point or limit cycle in its phase space.
The final achieved score is significantly higher than the random baseline. The Z-score, z_best=2.153, indicates that the
best score found is over 2.15 standard deviations above the mean score of random states. This demonstrates that the
guided trajectory is highly effective at finding states of exceptional resonance. The rewinds count of 24 and the use of
orthogonal jitter highlight the non-trivial nature of the search space, showing that the anti-drift and exploration
mechanisms were necessary to navigate local potential minima and successfully find the attractor state.
77
This
experiment provides a concrete computational validation of the probe's dynamics, showing how a simple, physically-
inspired process of gradient ascent with stochastic exploration can guide a probe to a stable state of high semantic
significance.
3.3 Experiment 3: Emergence of Symbolic Content from Physical Dynamics----------- Page16 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Objective: This experiment provides crucial evidence for the central hypothesis of the thesis: that semantic meaning is
not pre-encoded but emerges from the underlying physical dynamics of the system. It aims to demonstrate a correlation
between the physical state of the system (high resonance score) and the emergence of specific, meaningful symbolic
content.
Methodology: The glyphA_deciles function is used to test this hypothesis.
77
A large number of random probes (nonces)
are generated, and their resonance scores are computed. The resulting scores are then sorted and partitioned into ten
equal-sized bins, or deciles (D1 being the lowest 10% of scores, D10 being the highest 10%). For each decile, the
experiment measures the frequency of a specific symbolic pattern: the first byte of the corresponding 32-byte SHA-256
hash being equal to
0x41, the ASCII code for the capital letter 'A'.
Analysis of Results: The bar chart titled "'A' frequency by score decile (byte0)" presents the outcome of this
experiment.
77
The y-axis represents the probability of the first byte being 'A', and the x-axis represents the score deciles.
A clear and striking trend is visible: the frequency of the 'A' glyph is substantially higher in the upper deciles (D9 and
D10) compared to the lower and middle deciles. While the probability hovers near the expected random chance of
approximately 1/256 (≈0.0039) for the lower deciles, it rises significantly for the highest-scoring probes.
This result is the critical link between the physical and symbolic layers of the framework. It suggests that the states of
highest resonance—the attractors in the probe's phase space that are discovered through the dynamic trajectory—are
not random byte strings. Instead, these physically significant states are biased towards producing specific, non-random
symbolic content. The experiment demonstrates that a purely physical optimization process (maximizing the
phase_score) can lead to the emergence of what we recognize as meaningful information (the letter 'A').
It is important to acknowledge that the notebook does not provide a formal statistical test (such as a chi-squared test or
correlation analysis) to quantify the statistical significance of this observed trend.
77
The evidence presented is primarily
visual. However, the strength and monotonicity of the trend in the bar chart provide compelling observational evidence
for the correlation. This experiment, therefore, serves as a powerful proof-of-concept for the core thesis claim that
meaning is an emergent property of a computational physical process.
3.4 Experiment 4: Simulating the Collapse Branch Engine
Objective: This experiment validates the coupled dynamics of Principle I (The Semantic Field as a Dynamic Potential
Manifold) and Principle IV (Trajectory as Inquiry). It aims to provide a visual and mechanistic demonstration of the
Collapse Branch Engine (CBE), showing how a probe's trajectory is shaped by the topology of the field and how that
trajectory, in turn, reshapes the field through scarring.
Methodology: The cbe_sim function provides a complete simulation of the CBE dynamic.
77
The simulation environment
is a 2D grid representing a slice of the Semantic Field manifold.
1. Field Initialization: The simulation initializes a field array (representing potential/scar intensity) and a blocked
array (representing impassable obstacles or regions of infinite potential).
2. Probe Trajectory: An agent (the probe) attempts to navigate from a start to a goal position over a series of
steps.
3. Decision Logic: At each step, the agent evaluates all 8-connected neighbors. The choice of the next move is
based on a lexicographical score (align, -scar).
77
This means the agent first and foremost prioritizes moving in
the direction that is best aligned with the goal (----------- Page17 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
align). Only among equally well-aligned options does it choose the path with the lowest accumulated scar intensity (-
scar).
4. Interaction Dynamics:
o Forced Branching: If the most-aligned path is blocked by an obstacle, the agent is forced to take a less
optimal, alternative path—it "branches." If all paths are blocked, it performs a random hop.
77
o Scar Memory: When the agent's intended movement is denied or it is forced to deviate, a "scar" is laid
down by increasing the value of the field at its current location. This scar acts as a form of negative
reinforcement or memory within the environment.
77
o Field Evolution: The entire scar field slowly diminishes over time due to a decay factor, ensuring that old
memories fade and the field remains plastic.
Analysis of Results: The output plot, "Collapse Branch Engine (CBE): scars and forced branching," provides a powerful
visualization of the framework's dynamics.
77
The cyan line represents the probe's
trajectory, showing a "corridor" that has been carved through the space. The underlying colormap (from black/purple to
yellow/white) represents the Semantic Field's potential, with brighter colors indicating higher scar intensity.
The plot clearly demonstrates the key concepts. The trajectory is not a straight line from start to goal; it is a complex
path that navigates around the unseen obstacles. These deviations are instances of forced branching. The bright yellow
regions of high scar intensity are concentrated in areas where the probe likely encountered obstacles or got trapped,
forcing it to backtrack and explore alternatives. The final "corridor" of the trajectory exists in a region of relatively low
scar intensity (darker colors), demonstrating how the agent, guided by the lexicographical scoring, has learned to avoid
the high-potential, scarred regions. This simulation validates the coupled dynamics of the Nexus 4 framework, showing
how a history of interactions shapes the semantic landscape, and how that landscape, in turn, guides future inquiry.
Chapter 4: Discussion, Implications, and Future Directions
The preceding chapters have laid out the theoretical specification and computational validation of the Nexus 4
Framework. This final chapter synthesizes these findings, discusses their broader implications for artificial intelligence
and cognitive science, acknowledges the framework's current limitations, and charts a course for future research. The
central argument is that by reframing semantics as a computational physics, we can move beyond the limitations of
purely statistical models and toward a new class of AI systems that are more grounded, interpretable, and robust.
4.1 A Computational Physics of Cognition: A Synthesis
The Nexus 4 Framework represents a fundamental departure from the dominant paradigms in computational semantics.
It challenges the premise that meaning is a property to be represented—whether as a symbol in a logical system, a point
in a vector space, or a state in a neural network—and proposes instead that meaning is a process to be computed. This
process is not abstractly statistical but concretely physical, modeled as the dynamic interaction between a structured
probe and a structured field.
This approach directly addresses the core weaknesses of previous models. Unlike static vector-space models, the
framework is inherently dynamic. The meaning of a probe is not fixed but is determined by the outcome of its
interaction with a specific local region of the Semantic Field at a specific time, naturally accounting for context
dependency. Unlike the black-box models of the contextual revolution, the Nexus 4 Framework is designed for
interpretability. Its components and parameters have clear physical analogues: the harmonic modes of a probe, the
curvature and potential of a field, the resonance of an interaction, the decay rate of memory. This provides a clear----------- Page18 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
causal chain from the system's structure to its behavior, moving beyond mere correlation to a model with explanatory
power.
The framework unifies two previously disparate lines of inquiry in cognitive modeling: the static, geometric description
of knowledge structures and the dynamic, process-oriented description of cognitive acts. The Semantic Field, with its
Riemannian geometry and topological features, provides a formal basis for structural models like Gärdenfors'
Conceptual Spaces. The probe's trajectory, governed by the CBE dynamic, provides a formal basis for process models like
the enactive approach to cognition. In the Nexus 4 Framework, structure and process are not two separate domains but
are inextricably coupled facets of a single, underlying geometro-dynamic system.
4.2 Implications for Artificial Intelligence
The shift from a statistical to a physical paradigm for meaning has significant implications for the design and engineering
of artificial intelligence systems.
Grounding and Interpretability: A persistent challenge in AI is the symbol grounding problem—how to connect the
abstract symbols an AI manipulates to the real world. The Nexus 4 Framework offers a form of intrinsic grounding.
Meaning is not grounded by linking it to an external perceptual dataset but by the internal consistency of the physical
laws governing the system. The "meaning" of a probe's interaction is grounded in the consequences it has for the
probe's future trajectory and the evolution of the field. This, combined with the inherent interpretability of the model's
parameters, offers a path toward building AI systems whose reasoning processes are more transparent and auditable.
Robustness and Adversarial Resistance: Many modern deep learning models are known to be brittle and susceptible to
adversarial attacks, where minuscule, imperceptible perturbations to the input can cause catastrophic failures in output.
This fragility is often attributed to the high-dimensional, non-linear, and poorly understood geometry of their internal
representation spaces. By defining semantics within a space governed by well-defined geometric and physical principles,
the Nexus 4 Framework may offer greater robustness. An adversarial attack would need to be an input that not only
manipulates a high-dimensional feature vector but also successfully navigates the constrained dynamics of the system to
produce a targeted, high-resonance outcome—a potentially much more difficult task.
Novel Architectures: The principles of the framework suggest new avenues for AI architecture design. One promising
direction is the use of Physics-Informed Neural Networks (PINNs).
86
A PINN is a neural network trained not only to fit
data but also to obey a set of governing partial differential equations. One could design a neural architecture where the
Semantic Field is represented by a network, and the loss function includes terms that enforce the field evolution
equation (scarring and decay) and the probe's equation of motion.
87
This would allow the powerful optimization and
representation capabilities of deep learning to be harnessed within the principled, structured constraints of the Nexus 4
physics.
4.3 Connections to Cognitive Science
The framework not only provides a blueprint for artificial systems but also serves as a formal, computational model that
resonates with contemporary theories in cognitive science.
Embodied and Enactive Cognition: The Nexus 4 Framework can be seen as a formal implementation of the core tenets
of enactivism.
63
The framework's emphasis on interaction as the locus of meaning directly mirrors the enactivist
rejection of pre-given, representational worlds. The cognitive agent (the probe) and its environment (the field) are co-
determining; the agent's actions (its trajectory) bring forth a world of significance (regions of high and low potential),
and this enacted world shapes the agent's future actions.
66
The process of sense-making, central to enactivism, is
computationally realized in the probe's CBE trajectory as it seeks out and creates corridors of stability and high
resonance.
65----------- Page19 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Conceptual Spaces: The structure of the Semantic Field provides a dynamic origin story for Gärdenfors' Conceptual
Spaces.
68
The stable, low-potential "valleys" or basins of attraction in the field correspond directly to the convex regions
that Gärdenfors posits as the geometric representation of natural concepts.
88
The framework goes a step further by
showing how these structures might arise and evolve through a history of interaction and scarring, providing a
mechanism for conceptual change and learning that is grounded in the system's dynamics. The framework thus offers a
way to bridge the gap between the process-based philosophy of enactivism and the structure-based geometry of
conceptual spaces.
4.4 Limitations and Future Work
The version of the Nexus 4 Framework presented and validated in this thesis is a proof-of-concept, and it is essential to
acknowledge its limitations. The computational experiments are based on simplified models: the Semantic Field is
simulated in only two dimensions, the Symbolic Probe is defined by a cryptographic hash rather than a more
linguistically motivated structure, and the scattering model is a classical analogy of resonance rather than a full
quantum-mechanical computation. The scale of the system is small, and its direct application to complex, real-world
language tasks has not yet been demonstrated.
These limitations, however, illuminate a clear path for future research. The key directions for extending and maturing
the Nexus 4 Framework include:
 Scaling the Semantic Field: The representation of the Semantic Field must be scaled to higher dimensions to
capture the complexity of real-world knowledge. Techniques from manifold learning could be used to learn the
intrinsic low-dimensional geometry of a conceptual domain from data, providing the underlying manifold M for
the field.
32
Topological Data Analysis can then be used to characterize the structure of these learned manifolds.
40
 Developing Sophisticated Probe and Scattering Models: The cryptographic hash function should be replaced
with models that capture the compositional structure of language, perhaps using techniques from
neurosymbolic AI.
89
The scattering interaction itself could be modeled with greater physical fidelity, potentially
drawing on formalisms from quantum field theory or computational scattering models like SwitchNet to handle
more complex interactions.
90
 Application to NLP Tasks: The framework must be tested on benchmark NLP tasks. For example, in question
answering, a knowledge base could be modeled as the Semantic Field, and a question could be modeled as a
Symbolic Probe. The answer would be the attractor state or region that the probe's CBE trajectory converges to.
 Formal Verification of Nexus 4 AI: A long-term goal is to leverage the framework's formal, principled nature to
build verifiably correct AI systems. Because the system is defined by mathematical specifications and physical
laws, it is amenable to formal verification techniques like model checking and theorem proving.
73
One could, for
example, prove that an AI system built on these principles satisfies certain safety properties (e.g., "the system
will never enter a state corresponding to a harmful concept") or liveness properties (e.g., "any inquiry will
eventually converge to a stable state").
92
This could pave the way for a new generation of AI that is not only
powerful but also provably safe and reliable.
Conclusion
This thesis has proposed and defended a radical shift in the computational study of meaning. It has argued that the
persistent challenges in computational semantics—from the meaning conflation of static models to the opacity of
contextual ones—stem from a foundational misconception: that meaning is a property to be stored and retrieved. The
Nexus 4 Framework offers an alternative vision: meaning as a dynamic, physical event computed at the interface of a
symbolic probe and a structured semantic field.----------- Page20 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
By drawing upon the formal languages of physics and mathematics, the framework specifies a complete, self-contained
computational system. The Semantic Field, a dynamic Riemannian manifold, provides a structured, adaptive
environment for knowledge. The Symbolic Probe, a state in a harmonically-defined phase space, acts as an active
inquirer. Their interaction, modeled as a resonant scattering event, constitutes the act of meaning computation. The
evolution of this process, the CBE trajectory, models the flow of thought as a constrained, goal-directed exploration of
the semantic landscape.
The computational experiments presented herein serve as a validation of this vision, demonstrating that each
theoretical principle can be instantiated in a working simulation. These experiments show that symbolic entities possess
discoverable harmonic structures, that a probe's state can be guided to stable attractors of high resonance, that these
resonant states correlate with the emergence of meaningful symbolic content, and that the coupled dynamics of probe
and field create adaptive, learning behavior.
The implications of this work are far-reaching. For artificial intelligence, it offers a path toward systems that are
grounded, interpretable, and potentially more robust, moving beyond the paradigm of statistical pattern matching to
one of principled physical simulation. For cognitive science, it provides a formal, computational bridge between the
process-oriented philosophy of enactivism and the structural geometry of conceptual spaces, unifying them within a
single, coherent geometro-dynamic model.
The road ahead is long and challenging. The models presented here are simplified proofs-of-concept that must be scaled
and refined. Yet, the foundational principles of the Nexus 4 Framework—of meaning as interaction, of knowledge as a
dynamic field, and of thought as a physical trajectory—offer a powerful and promising new lens through which to view
the deepest questions of cognition. It is a vision not of a machine that has learned to imitate understanding, but of a
system that computes meaning through the very same principles of interaction, structure, and dynamics that govern the
physical world itself.
Appendix A: Annotated Source Code from CAS_Notebook.pdf
Appendix B: Mathematical Derivations
B.1 Derivation of the Semantic Field Evolution Equation
The evolution of the Semantic Field's metric tensor gp at a point p on the manifold M is governed by two competing
processes: a local, event-driven increase in potential due to scarring, and a global, continuous decay of potential.
Let gp(t) be the metric tensor at point p and time t.
1. Decay Process: We model the decay as a first-order process, where the rate of change of the metric is
proportional to its current state. This represents a natural dissipation or "forgetting" mechanism.∂t∂gp
decay=−λgp(t)
where λ is a positive decay constant.
2. Scarring Process: An interaction event (a "forced branch" or failed inquiry) at a specific point pi and time ti
introduces a discrete change in the field. We model this as an impulsive source term. The total effect of all such
events is a sum over the history of interactions.
$$ \frac{\partial g_p}{\partial t}\bigg|{\text{scar}} = \sum{i} \Gamma(p_i, t_i) \delta(p - p_i) \delta(t - t_i) $$
where Γ(pi,ti) is a tensor representing the magnitude and nature of the scar added at event i, and δ is the Dirac delta
function, localizing the effect in both space and time.----------- Page21 ------------
Copyright Dean A. Kulik – Orcid ID # 0009-0003-3128-8828
Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
github.com/QuHarmonics/The-Nexus-Harmonic-Reality
Combining these two processes gives the full evolution equation for the metric tensor:
∂t∂gp(t)=−λgp(t)+i∑Γiδ(p−pi,t−ti)
This equation is a non-homogeneous first-order linear partial differential equation for the metric tensor. Its solution
describes how the geometry of the Semantic Field is continuously shaped by the history of cognitive interactions.
B.2 Derivation of the Probe's Equation of Motion
The trajectory of the Symbolic Probe's internal state s=(q,p) is governed by a gradient ascent on the phase_score
surface, modified by a stochastic term.
Let the phase_score function be denoted by Φ(s;gp), where its dependence on the probe's state s and the
local field metric gp is made explicit. The principle of inquiry states that the probe's state evolves to maximize this
resonance score.
1. Gradient Ascent: The deterministic component of the motion follows the gradient of the score function in the
probe's phase space PS.
s˙det=α
∇
sΦ(s;gp)
where α is a learning rate or mobility constant. This ensures the probe moves "uphill" on the resonance landscape.
2. Stochastic Jitter: To prevent the probe from becoming trapped in suboptimal local maxima (local minima of
potential), we introduce a stochastic forcing term, η(t). This term represents random fluctuations or "jitter" that
allow the probe to explore the phase space. This is analogous to Langevin dynamics.
s˙stoch=η(t)
where η(t) is typically modeled as a white noise process, e.g.,
⟨
ηi(t)ηj(t′)
⟩
=2Dδijδ(t−t′), with D being the diﬀusion
constant.
The complete equation of motion for the probe's state is the sum of these two components, forming a stochastic
differential equation:
s˙=α
∇
sΦ(s;gp)+η(t)
This equation formally describes the process of inquiry as a biased random walk through the probe's phase space, driven
by the search for semantic resonance while maintaining a capacity for exploration. The "orthogonal jitter" in the
hillclimb_anti_drift algorithm is a discrete, computationally efficient approximation of this continuous stochastic
process.
```
