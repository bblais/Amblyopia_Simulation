#!/usr/bin/env python
# coding: utf-8

# # Results
# 
# ## Deficit and Measuring the Effectiveness of a Treatment
# 
# Figure @fig:y_vs_t_fix_n0 shows the maximum response to oriented stimuli for $n=20$ neurons versus time.  The first 8 days of simulated time define the *deficit* period, where the neurons start in a naïve state with random synaptic weights, and are presented with natural image input blurred in the weak-eye channel as in Section @sec:methods.  Following the deficit, the simulation proceeds into the *fix* period, where the balanced natural image input is restored.  This transition is marked with a red line in Figure @fig:y_vs_t_fix_n0.  We can see only a modest improvement in the deprived-eye responses to the *fix* treatment.  This treatment depends on the noise level presented to the open eye.  In Figure @fig:y_vs_t_fix_n0, that noise level is $\sigma_n = 0$ whereas in Figure @fig:y_vs_t_fix_n1 the noise level is $\sigma_n=1$.  Increasing the open-eye noise results in an improved recovery from the deficit.  
# 
# Figure @fig:ODI_vs_t_fix_n1 shows a measurement of this recovery, using the oculur dominance index described in Section @sec:ocular-dominance-index.  Balance responses result in an $\text{ODI}=0$.  As the deficit is increased, so the ODI increases toward 1.  After the fix, with high levels of open-eye noise, the neurons nearly all recover from much of their initial deficit -- the ODI nearly returns to $\text{ODI}=0$.  A simple measure of the effectiveness of the treatment is the *rate* of the recovery of the ODI:
# 
# $$
# \text{recovery rate}=\frac{ODI_{\text{deficit}}-ODI_{\text{treatment}}}{\text{duration of treatment}}
# $$
# 
# ## Recovery using glasses
# 
# The "fix" treatment described in Section @sec:models-of-development-and-treatment-of-amblyopia and Section @sec:deficit-and-measuring-the-effectiveness-of-a-treatment depends on the noise level in the open eye.  Figure @fig:dODI_fix_vs_noise shows the rate of recovery as a function of this noise.  For low-noise, there is very little improvement.  For large noise, $\sigma_n=1$, the rate achieves 0.14 [ODI/day].  This measure lets us compare different treatments, and determine which are the most effective under the model assumptions.                Because the experimental observation is that glasses alone are only able to fully restore vision in 27% of amblyopia cases[@wallace2006treatment], the other simulations use an open-eye noise value of $\sigma_n=0.1$.  
# 
# 
# ## Patch Treatment
# 
# As shown in @sec:results, increased *unstructured* input into the previously dominant eye increases the rate of recovery.  This is a general property of the BCM learning rule and has been explored elsewhere[@BlaisEtAl99].
# 
# 
# Figure @fig:dODI_patch_vs_noise shows the effect of the patch treatment as a function of the closed-eye noise.   For noise levels above $\sigma_n \sim 0.4$ the patch treatment is more effective than recovery with glasses alone.  There is the danger of the patch treatment and some other treatments (see below) of causing reverse amblyopia, producing a deficit in the previously stronger eye.  This will be dependent on the magnitude of the initial deficit and the amount of time for the treatment.  Because the BCM learning rule works by the competition between patterns, there is no danger of causing reverse amblyopia with the fix with glasses, but there is that danger in any treatment that has an asymmetry between the strong and weak eye, favoring the weak eye, as most treatments have.
# 
# #todo 
# - [ ] example of reverse amblyopia
# 
# 
# 
# ## Atropine Treatment
# 
# Figure @fig:dODI_atropine_vs_blur shows the recovery rates under the atropine treatment, where the strong eye is presented with a blurred, noisy version of the natural input.  Like the patch treatment, the effect is increased with increasing noise level due to the competition between patterns.  When the blur filter is very small, the strong-eye inputs are nearly the same as the weak-eye inputs, yielding a result much like the glasses fix.  When the blur filter is larger, the atropine treatment becomes comparable to the patch treatment.  The blurred inputs are no better than the patch treatment, which has only the noise input.  
# 
# 
# ## Contrast Modification and Dichoptic Masks
# 
# 
# Figure @fig:dODI_constrast shows the recovery rates under a binocular treatment which only involves contrast modification, where the contrast for the strong-eye is adjusted relative to the weak eye.  A contrast level of 1 is normal equal-eye vision.  A contrast level of 0 means that the strong-eye input is shut off entirely.  We see an increased rate of recovery with a smaller contrast value, or a larger difference between the strong- and weak-eye inputs.  The rate does not compare to the rate of the patch treatment, because while there is a larger difference between the strong- and weak-eye inputs for lower contrast value, the rate of change of the strong-eye weights is decreased.  The patch and atropine treatments result in more competition between patterns, resulting in faster recovery times.
# 
# #todo 
# - [ ] discuss optimal contrast level
# 
# Figure @fig:dODI_constrast_mask shows the recovery rates under a binocular treatment which includes both contrast modification and dichoptic masks.  The effect of the mask is diminished as the mask filter size increases, which is expected because a larger filter size results in more overlap in the strong- and weak-eye inputs and thus less competition.  Interestingly, the mask enhances the effect of contrast on the recovery rates in two ways.  For low contrast value (i.e. strong- and weak-eye inputs are more different) the mask increases the recovery rate and can reach rates comparable or exceeding patch treatment.  For extremely low contrast values, where nearly all of the input is coming in from the weak eye, there is possibility of causing reverse amblyopia.  For high contrast value (i.e. strong- and weak-eye inputs are nearly the same), the masks not only make the recovery slower, but can even enhance the amblyopia.
# 
# 

# In[ ]:




