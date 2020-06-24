def merge_meetings(times):
    times.sort()

    merged_meetings = [times[0]]
    merged_start = merged_meetings[0][0]
    merged_end = merged_meetings[0][1]
    meeting_index = 0

    print times
    for meeting in times:
        start = meeting[0]
        end = meeting[1]

        print "Meeting: %s   Start: %s   End: %s" % (meeting, start, end)
        print "Merge Start: %s   Merge End: %s" % (merged_start, merged_end)
        if end >= merged_end and start >= merged_start and start <= merged_end:
            merged_end = end
            merged_meetings[meeting_index][1] = end
        elif start > merged_end:
            meeting_index += 1
            merged_start = start
            merged_end = end
            merged_meetings.append([start, end])

        print merged_meetings

    return merged_meetings


def main():
    meeting_times = [[1, 10], [7, 8], [2, 4], [2, 5], [1, 4], [7, 9]]
    print(merge_meetings(meeting_times))  #


if __name__ == '__main__':
    main()
