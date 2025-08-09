Acceptance checklist (copy to CI):

- Response shape: array of 4 strings for the wiki prompt
- Element[0] equals integer count as string
- Element[1] contains earliest movie title as string
- Element[2] is correlation as string with 6 decimals
- Element[3] is data URI starting with data:image/...;base64, and decoded bytes <100000
- Axis labels in plot MUST be 'Rank' and 'Peak'
- Regression line must be dotted and red
- Total response time < 180 seconds (aim 150s)
