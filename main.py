import psycopg2
from psycopg2.extras import RealDictCursor


if __name__ == '__main__':
    conn = psycopg2.connect("host=pgdatabase dbname=aggregations user=root password=root", cursor_factory=RealDictCursor)
    cur = conn.cursor()

    """ Create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE IF NOT EXISTS table_a
        (
            dimension_1 varchar(1),
            dimension_2 varchar(1),
            dimension_3 varchar(1),
            measure_1 integer
        )
        """,
        """
        INSERT INTO table_a(dimension_1, dimension_2, dimension_3, measure_1)
            VALUES
            ('a', 'I', 'K', 1),
            ('a', 'J', 'L', 7),
            ('b', 'I', 'M', 2),
            ('c', 'J', 'N', 5)
        """,
        """
        CREATE TABLE IF NOT EXISTS table_b
        (
            dimension_1 varchar(1),
            dimension_2 varchar(1),
            measure_2 integer
        )
        """,
        """
        INSERT INTO table_b(dimension_1, dimension_2, measure_2)
            VALUES
            ('a', 'J', 7),
            ('b', 'J', 10),
            ('d', 'J', 4)
        """,
        """
        CREATE TABLE IF NOT EXISTS table_map
        (
            dimension_1 varchar(1),
            correct_dimension_2 varchar(1)
        )
        """,
        """
        INSERT INTO table_map(dimension_1, correct_dimension_2)
            VALUES
            ('a', 'W'),
            ('a', 'W'),
            ('b', 'X'),
            ('c', 'Y'),
            ('b', 'X'),
            ('d', 'Z')
        """
    )

    for command in commands:
            cur.execute(command)

    cur.execute(
        """
        SELECT
            dimension_1,
            dimension_2,
            COALESCE(SUM(measure_1), 0) AS measure_1,
            COALESCE(SUM(measure_2), 0) AS measure_2
        FROM (
            SELECT DISTINCT
                a.dimension_1,
                correct_dimension_2 AS dimension_2,
                measure_1,
                CAST(NULL AS INT) AS measure_2
            FROM table_map AS m
            INNER JOIN table_a AS a
                ON m.dimension_1 = a.dimension_1

            UNION

            SELECT DISTINCT
                b.dimension_1,
                correct_dimension_2 AS dimension_2,
                CAST(NULL AS INT) AS measure_1,
                measure_2
            FROM table_map AS m
            INNER JOIN table_b AS b
                ON m.dimension_1 = b.dimension_1
        ) temp
        GROUP BY dimension_1, dimension_2
        ORDER BY 1
        """
    )

    results = cur.fetchall()

    for row in results:
          print(row)
