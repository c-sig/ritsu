ritsu will be a project management tool meant to completely automate things relevant to scanlation group management. this generally means staff logging and series logging.

ritsu will primarily be used as a discord bot.

the goal of ritsu is to make everything completely transparent while maintaining anonymity for things that should stay anonymous.

a checklist of important stuff:
- [ ] docker
- [ ] work out CI/CD as this will be deployed to docker continuously for simplicity and to allow people to contribute directly
- [ ] proper logging to file, stdout, and discord or email
- [ ] concrete database that should cover all potential usecases (as much data as possible)
- [ ] staff, group, series, chapter, page, qualification, etc. functions
- [ ] proper configuration file for permissions, setups, etc.
- [ ] job functions

good features:
- [ ] make qc more open
- [ ] different credit names
- [ ] conditional dibs system
- [ ] proper rendering. ui components with pages, dropdowns, buttons, modals, etc for ease of use
- [ ] dm/ping users for vacant jobs theyre eligible for (opt out)
- [ ] if member takes more than x days for a job, remind or remove them. should be customizable
- [ ] job locking, jobs that can be done are the only things that should be claimed
- [ ] staff leaderboards
- [ ] dm project manager when project theyre managing has a job that got finished with the details and job done
- [ ] only display jobs that have not been claimed yet per series
- [ ] enable ability for simulwork
- [ ] priority settings
- [ ] check how far behind current compared to raws
- [ ] proper raw reminding (track releases and possibly automate chapter creation)
- [ ] list people by role
- [ ] credit page automation
- [ ] reputation