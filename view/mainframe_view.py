
import configuration.log_details as log

class MainframeView:

    def __call__(self, Matrix):
        """Returns Universe Map as String."""
        universeString = ''

        for y, row in enumerate(Matrix):
            first_line = ''
            second_line = ''

            for x, point in enumerate(row):

                log.log('Drawing %s' % point, level=10)
                first_line += point[0]
                second_line += point[1]

            universeString += first_line + '\n' + second_line + '\n'

        return universeString

class ViewFabric:

    def __call__(self, main_vm, mapIdents):

        if main_vm.atSection:
            section_window = self.section_view(main_vm)
            return [section_window], main_vm.anomaly.coordinates

        if main_vm.atAnomaly:
            anomaly_window = self.anomaly_view(main_vm)
            return [anomaly_window], main_vm.anomaly.coordinates

        uv_windows, uv_positions = self.universe_view(main_vm, mapIdents)
        return uv_windows, uv_positions

    def universe_view(self, availableAnomalies, mapIdentifiers):
        windows = list()
        positions = list()

        for anomaly in availableAnomalies:
            win = mapIdentifiers[anomaly.__class__.__name__]
            pos = anomaly.coordinates

            if anomaly == availableAnomalies.active:
                win = mapIdentifiers['Highlight']

            if anomaly == availableAnomalies.current:
                win = mapIdentifiers['Current']

            win = win[0] + '\n' + win[1]

            windows.append(win)
            positions.append(pos)

        return windows, positions

    def anomaly_view(self, availableSections):
        sectionInfo = 'Welcome to %s %s\n' % (self.act_anmy.__class__.__name__, self.act_anmy.name)
        for i, section in enumerate(availableSections):
            sectionInfo += " [%s] %s\n" % (i, section.infoString())

        return sectionInfo

    def section_view(self, Section):
        # Build Information
        interactionInfo = ''

        interactionInfo += "%s %s" % (self.act_anmy.__class__.__name__, self.act_anmy.name)

        interactionInfo += " -- %s\n"  % Section.infoString()

        interactionInfo += " [0] Back\n"

        for i, item in enumerate(Section):
            interactionInfo += " [%s] %s for %s\n" % (i+1, item.name, item.price)

        return interactionInfo
