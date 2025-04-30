from robot.api import logger

class ReportListener:
    ROBOT_LISTENER_API_VERSION = 3

    def __init__(self):
        self.failed_tests = []

    def end_test(self, name, attributes):
        # attributes[0] is the test's status
        # attributes[1] is the failure message (if any)
        test_status = attributes.status
        test_message = attributes.name

        if test_status == 'FAIL':
            self.failed_tests.append({
                "name": name,
                "message": test_message
            })
    
    # def end_test(self, name, attributes):
    #     # DEBUG: Inspect attributes
    #     print(f"DEBUG: end_test called with name={name}, attributes={attributes}")

    #     try:
    #         # Check if attributes has status and message
    #         if isinstance(attributes, dict):
    #             # Normal dictionary handling
    #             if attributes['status'] == 'FAIL':
    #                 self.failed_tests.append({
    #                     "name": name,
    #                     "message": attributes['message']
    #                 })
    #         elif hasattr(attributes, 'status') and hasattr(attributes, 'message'):
    #             # Handle attributes as an object
    #             if attributes.status == 'FAIL':
    #                 self.failed_tests.append({
    #                     "name": name,
    #                     "message": attributes.message
    #                 })
    #         else:
    #             print(f"DEBUG: Unknown attributes format: {attributes}")
    #     except Exception as e:
    #         print(f"Error in end_test: {e}")

    def close(self):
        try:
            with open('reports/report.html', 'r', encoding='utf-8') as file:
                report_content = file.read()

            # Create a custom section for failed tests
            custom_section = """
            <div style="border: 2px solid #FF0000; padding: 10px; margin: 10px;">
                <h2 style="color: #FF0000;">Custom Section: Failure Details</h2>
                <ul>
            """
            for test in self.failed_tests:
                custom_section += f"<li><strong>{test['name']}:</strong> {test['message']}</li>"
            custom_section += "</ul></div>"

            # Add the custom section before the closing </body> tag
            updated_content = report_content.replace("</body>", f"{custom_section}</body>")

            with open('reports/report.html', 'w', encoding='utf-8') as file:
                file.write(updated_content)

            logger.console("Custom section added to report.html successfully.")
        except Exception as e:
            logger.console(f"Failed to modify report.html: {e}")
