WITH TeacherGradedAssignments AS (
    SELECT 
        teacher_id,
        COUNT(*) AS graded_count
    FROM 
        assignments
    WHERE 
        state = 'GRADED'
    GROUP BY 
        teacher_id
),
TopTeacher AS (
    SELECT 
        teacher_id
    FROM 
        TeacherGradedAssignments
    ORDER BY 
        graded_count DESC
    LIMIT 1
)

SELECT 
    COUNT(*) AS grade_A_count
FROM 
    assignments
WHERE 
    state = 'GRADED'
    AND grade = 'A'
    AND teacher_id = (SELECT teacher_id FROM TopTeacher);
