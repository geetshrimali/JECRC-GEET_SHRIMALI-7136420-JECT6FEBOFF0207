#Hospital Patient Visit Counter

class Solution:

    def department_patient_count(self, visits):
        dept_count = {}
        ## Write your code here & Don't forget to add return keyword
        for visit in visits:
            department = visit["department"]

            if department not in dept_count:
                dept_count[department] = 1
            else:
                dept_count[department] = dept_count[department] + 1

        max_department = ""
        max_count = 0

        for department in dept_count:
            if dept_count[department] > max_count:
                max_count = dept_count[department]
                max_department = department

        return dept_count, max_department